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


import pytest;
import ada;
import re;

def test_default(app, match):
	
	app.message('register user');
	app.message('start');
	
	stage     = app.database.repos.deliveries.get_stage();
	delivery  = app.database.repos.deliveries.get_current();
	gathering = delivery.re_gathering;
	
	assert stage == ada.entities.Stage.GATHER;
	assert match(r"^Delivery\(id=1, started=.*, stage=Stage.GATHER, ignored=False, ended=None, log_start=2, log_end=None\)$", delivery);
	assert match(r"^Gathering\(id=1, started=.*, timeout=None, ended=None\)$", gathering);

def test_skipping(app, match):
	
	app.message("register root");
	app.message("rest-add rest");
	app.message("start rest");
	
	stage     = app.database.repos.deliveries.get_stage();
	delivery  = app.database.repos.deliveries.get_current();
	gathering = delivery.re_gathering;
	voting    = gathering.re_voting;
	order     = voting.re_order;
	
	# TODO: Endeds?
	assert stage == ada.entities.Stage.ORDER;
	assert match(r"^Delivery\(id=1, started=202.*, stage=Stage.ORDER, ignored=False, ended=None, log_start=3, log_end=None\)$", delivery);
	assert match(r"^Gathering\(id=1, started=202.*, timeout=None, ended=None\)$", gathering);
	assert match(r"^Voting\(id=1, started=202.*, timeout=None, ended=None, winner=1\)$", voting);
	assert match(r"^Order\(id=1, started=202.*, timeout=None, ended=None\)$", order);

#	app.message('config TIMEOUT-GATHER 10');

