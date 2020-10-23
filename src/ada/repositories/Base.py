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

from .. import entities;
from sqlalchemy.sql import func;
import ada;
import re;

# Declaration of extra methods for base SQLAlchemy model classes
class Base():
	
	entity = None;
	
	def __init__(self,
			session,
			entity  = None):
		
		if not entity:
			entity = self.entity;
		
		self.session = session;
		self.entity  = entity;
		self.init();
	
	def init(self):
		pass;
	
	def query(self):
		"""
			Return sqlalchemy query object for this repository entity.
		"""
		
		query = self.session.query(self.entity);
		
		return query;
	
	def get(self, **filters):
		"""
			Generate sqlalchemy query with filters from arguments.
		"""
		
		query = self.query();
		
		for key,value in filters.items():
			column = getattr(self.entity, key);
			query  = query.filter(column == value);
		
		return query;
	
	def get_one(self,
			**filters):
		"""
			Return one sqlalchemy object selected by filters from arguments.
		"""
		
		item = self.get(**filters).one_or_none();
		
		return item;
	
	def get_all(self,
			**filters):
		"""
			Return all sqlalchemy object selected by filters from arguments.
		"""
		
		items = self.get(**filters).all();
		
		return items;
	
	def get_ex(self,
			**filters):
		"""
			Return exactly one sqlalchemy object selected by filters from
			arguments or raise an exception.
		"""
		
		items = self.get_all(**filters);
		
		if not items:
			msg = "";
			raise Exception(msg);
		
		if len(items) > 1:
			msg = "";
			raise Exception(msg);
		
		return items[0];

