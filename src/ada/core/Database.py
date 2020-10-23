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

import ada;
import pathlib;
import sqlalchemy;
import sqlalchemy.ext.declarative;
import sqlalchemy.orm.session;
import types;

class Database:
	"""
		Class for creating and holding SQLAlchemy database session, with
		additional metadata.
		
		Attributes:
			file
			echo
			connstr
			engine
			smaker
			session
			repos
	"""
	
	def __init__(self,
			base_ents  : sqlalchemy.ext.declarative.api.DeclarativeMeta,
			base_repos : object       = None,
			file       : pathlib.Path = None,
			echo       : bool         = False):
		"""
			Create new SQLAlchemy database session and store additional metadata.
			If database structure does not exists, then create it.
			
			Arguments:
				base_ents
				base_repos
				file
				echo
		"""
		
		# Prepare connection string
		connstr = f"sqlite:///{file or ':memory:'}";
		
		# Create new database session
		engine  = sqlalchemy.create_engine(connstr, echo=echo);
		smaker  = sqlalchemy.orm.session.sessionmaker(bind=engine);
		session = smaker();
		
		# If required, then build database
		base_ents.metadata.create_all(engine);
		
		# Create namespace for repositories instances
		repos = types.SimpleNamespace();
		
		# If repositories base class is given,
		# then create instance of each subclass of a repositories
		# base class and add it to repositories namespace
		if base_repos:
			for subclass in base_repos.__subclasses__():
				name = subclass.__name__.lower();
				obj  = subclass(session);
				setattr(repos, name, obj);
		
		# Save session and its metadata
		self.file    = file;
		self.echo    = echo;
		self.connstr = connstr;
		self.engine  = engine;
		self.smaker  = smaker;
		self.session = session;
		self.repos   = repos;

