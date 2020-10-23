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

from sqlalchemy     import *;
from sqlalchemy.orm import *;
from sqlalchemy.ext import declarative;
from datetime       import datetime;

@declarative.as_declarative()
class Base():
	
	__repr_list__ = tuple();
	
	def __repr__(self):
		
		# Get name of the class
		name = self.__class__.__name__;
		
		# Add id to list of attributes
		attrs = ("id",) + self.__repr_list__;
		
		# Get value of each attribute from list
		values = [(attr, getattr(self, attr)) for attr in attrs]
		
		# Join attributes names and values
		values = [f"{attr}={value}" for attr,value in values];
		
		# Join each attributes value
		values = ", ".join(values);
		
		# Return formatted values of object attributes
		return f"{name}({values})";

