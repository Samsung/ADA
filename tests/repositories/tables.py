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

def test(database):
	"""
		Check if each table has its own repository.
	"""
	
	# Select list of created tables in alphabetical order
	query  = "SELECT name FROM sqlite_master WHERE type ='table';";
	result = database.engine.execute(query).fetchall();
	tables = sorted([row[0] for row in result]);
	
	# For each existing table
	for table in tables:
		
		# Create new repository
		cls = getattr(ada.repositories, table);
		obj = cls(database.session);
		
		# Query for all records (even if table is empty)
		result = obj.get_all();
		
		# Basic assertion
		assert result == [];

