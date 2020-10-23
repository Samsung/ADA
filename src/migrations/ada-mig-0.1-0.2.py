#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
#    Copyright (C) 2020 Samsung Electronics. All Rights Reserved.
#       Authors: Anonymous Cat (Samsung R&D Poland)
#
#    This file is part of ADA.
#
#    ADA is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 2 of the License, or
#    (at your option) any later version.
#
#    ADA is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with ADA. If not, see <http://www.gnu.org/licenses/>.
#

"""
	Script to migrate ADA database file from version 0.1 to version 0.2.
	It was used once on backup file: 320619af7bac529ab75e1a498a74238d57468754.
"""

################################################################################

import ada;
import collections;
import dateutil.parser;
import pathlib;
import re;
import sqlalchemy;
import sys;
import types;

################################################################################
# Parse command line arguments

if len(sys.argv) != 3:
	print("Script for migrating ADA database file from version 0.1 to version 0.2.");
	print("Usage:", sys.argv[0], "old_database_file_path new_database_file_path");
	quit();

database_path_old = pathlib.Path(sys.argv[1]);
database_path_new = pathlib.Path(sys.argv[2]);

if not database_path_old.is_file():
	print("ERROR: Old database file does not exists!");
	quit();

if database_path_new.exists():
	print("ERROR: New database file already exists!");
	quit();

################################################################################
# Connect to databases

argv = ["-t", "0", "-d", str(database_path_new)];
app  = ada.core.ApplicationMock(argv);

connstr = f"sqlite:///{database_path_old}";
engine  = sqlalchemy.create_engine(connstr);
smaker  = sqlalchemy.orm.session.sessionmaker(engine);
session = smaker();

################################################################################
# Function for selecting all data from single table

def table_dump(session, table):
	
	query = f"SELECT * FROM {table}";
	cols  = session.execute(query).keys();
	rows  = session.execute(query).fetchall();
	data  = collections.OrderedDict();
	
	for row in rows:
		temp   = dict(zip(cols, row));
		entity = types.SimpleNamespace(**temp);
		data[entity.id] = entity;
	
	return data;

################################################################################
# Create namespace for old data schema

query  = "SELECT name FROM sqlite_master WHERE type ='table';";
result = session.execute(query).fetchall();
tables = sorted([row[0] for row in result]);
data   = {t.lower():table_dump(session, t) for t in tables};
nso    = types.SimpleNamespace(**data);

################################################################################
# Create namespace for new data schema

query  = "SELECT name FROM sqlite_master WHERE type ='table';";
result = app.database.session.execute(query).fetchall();
tables = sorted([row[0] for row in result]);
data   = {t.lower():collections.OrderedDict() for t in tables};
nsn    = types.SimpleNamespace(**data);

################################################################################
# Helpers for simplify data mapping

def mass_mapper(nso, nsn, cls_name, map_fun, *args):
	
	cls  = getattr(ada.entities, cls_name);
	attr = cls.__tablename__.lower();
	olds = getattr(nso, attr);
	
	print("#"*80, cls_name);
	print("#", olds.get(1));
	print();
	
	for key,old in olds.items():
		print(old);
		new = map_fun(nso, nsn, cls, old, args);
		getattr(nsn, attr)[key] = new;
		new.id = old.id;
		app.database.session.add(new);
		print(new);

def mass_mapper_decorator(mapper):
	cls_name = mapper.__name__.split("_")[1].capitalize();
	mass_mapper(nso, nsn, cls_name, mapper);

################################################################################ Log

@mass_mapper_decorator
def mapper_log(nso, nsn, cls, old, args):
	return cls(
			date     = dateutil.parser.parse(old.date),
			sender   = int(re.search("^<@!?([0-9]+)>$", old.user).group(1)),
			receiver = 516601388181094411,
			channel  = "fooood",
			content  = old.text,
			is_input = True,
			delivery = old.delivery,
	);

################################################################################ User

# Find user last action
actions = dict();
for key,log in nsn.logs.items():
	actions[log.sender] = log;

@mass_mapper_decorator
def mapper_user(nso, nsn, cls, old, args):
	
	did = int(re.search("^<@!?([0-9]+)>$", old.mention).group(1));
	register = [l for k,l in nsn.logs.items() if l.sender == did and l.content.startswith("<@516601388181094411> register")][0];
	
	if register.id != old.log:
		raise Exception();
	
	return cls(
			did         = did,
			nick        = old.nick,
			role        = old.role+10,
			log_created = register,
			log_action  = actions[did],
			log_role    = register,
	);

################################################################################ Restaurant

@mass_mapper_decorator
def mapper_restaurant(nso, nsn, cls, old, args):
	return cls(
			key         = old.name,
			name        = old.name,
			url         = old.url,
			active      = True,
			log_created = nsn.logs[old.log],
			log_action  = nsn.logs[old.log],
	);

################################################################################ Transfer
if len(nso.transfers) > 1:
	raise Exception();

################################################################################ Delivery

@mass_mapper_decorator
def mapper_delivery(nso, nsn, cls, old, args):
	return cls(
			started   = dateutil.parser.parse(old.started),
			stage     = old.stage,
			ignored   = old.ignored,
			ended     = dateutil.parser.parse(old.ended),
			log_start = nsn.logs[old.logStart],
			log_end   = nsn.logs[old.logEnd],
	);

################################################################################ Gathering

@mass_mapper_decorator
def map_gathering(nso, nsn, cls, old, args):
	return cls(
			delivery = nsn.deliveries[old.id],
			started  = dateutil.parser.parse(old.started),
			timeout  = dateutil.parser.parse(old.timeout) if old.timeout else None,
			ended    = dateutil.parser.parse(old.ended)   if old.ended   else None,
	);

################################################################################ Candidate

@mass_mapper_decorator
def map_candidate(nso, nsn, cls, old, args):
	return cls(
			gathering  = nsn.gatherings[old.gathering],
			restaurant = nsn.restaurants[old.restaurant],
			log        = nsn.logs[old.log],
	);

################################################################################ Voting

@mass_mapper_decorator
def map_voting(nso, nsn, cls, old, args):
	return cls(
			gathering = nsn.gatherings[old.id],
			started   = dateutil.parser.parse(old.started),
			timeout   = dateutil.parser.parse(old.timeout) if old.timeout else None,
			ended     = dateutil.parser.parse(old.ended)   if old.ended   else None,
			winner    = nsn.candidates[old.winner]         if old.winner  else None,
	);

################################################################################ Vote

@mass_mapper_decorator
def map_vote(nso, nsn, cls, old, args):
	return cls(
			voting    = nsn.votings[old.voting],
			voter     = nsn.users[old.voter],
			candidate = nsn.candidates[old.candidate],
			value     = old.value,
			log       = nsn.logs[old.log],
	);

################################################################################ Order

@mass_mapper_decorator
def map_order(nso, nsn, cls, old, args):
	return cls(
			voting  = nsn.votings[old.id],
			started = dateutil.parser.parse(old.started),
			timeout = dateutil.parser.parse(old.timeout) if old.timeout else None,
			ended   = dateutil.parser.parse(old.ended)   if old.ended   else None,
	);

################################################################################ Item

@mass_mapper_decorator
def map_item(nso, nsn, cls, old, args):
	return cls(
			order     = nsn.orders[old.order],
			purchaser = nsn.users[old.purchaser],
			price     = int(round(round(float(old.price), 2)*100, 0)),
			note      = old.text,
			log       = nsn.logs[old.log],
	);

################################################################################ Summary

@mass_mapper_decorator
def map_summary(nso, nsn, cls, old, args):
	return cls(
			order   = nsn.orders[old.id],
			started = dateutil.parser.parse(old.started),
			ended   = dateutil.parser.parse(old.ended) if old.ended else None,
	);

################################################################################ Payment

@mass_mapper_decorator
def map_payment(nso, nsn, cls, old, args):
	if old.price is None:
		raise Exception();
	if type(old.price) not in [int, float]:
		raise Exception();
	return cls(
			summary = nsn.summaries[old.id],
			payer   = nsn.users[old.payer],
			price   = int(round(round(float(old.price), 2)*100, 0)),
			etofa   = dateutil.parser.parse(old.etofa) if old.etofa else None,
			log     = nsn.logs[old.log],
	);

################################################################################ Adjustment

@mass_mapper_decorator
def map_adjustment(nso, nsn, cls, old, args):
	return cls(
			summary = nsn.summaries[old.id],
			started = dateutil.parser.parse(old.started),
			ended   = dateutil.parser.parse(old.ended) if old.ended else None,
			log     = nsn.logs[old.log]                if old.log   else None,
	);

################################################################################ Correction

@mass_mapper_decorator
def map_correction(nso, nsn, cls, old, args):
	if old.price is None:
		raise Exception();
	if type(old.price) not in [int, float]:
		raise Exception();
	return cls(
			adjustment = nsn.adjustments[old.adjustment],
			corrector  = nsn.users[old.corrector],
			purchaser  = nsn.users[old.purchaser],
			price      = int(round(round(float(old.price), 2)*100, 0)),
			note       = old.note,
			log        = nsn.logs[old.log],
	);

################################################################################
# Save data into database

app.database.session.commit();
print("DONE!");

