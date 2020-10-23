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
	
	# Select list of created tables in alphabetical order
	query   = "SELECT name FROM sqlite_master WHERE type ='table';";
	result  = database.engine.execute(query).fetchall();
	created = sorted([row[0] for row in result]);
	
	# Gather list of all entity tables in alphabetical order
	entities = [v for k,v in ada.entities.Base.metadata.tables.items()];
	defined = sorted([entity.fullname for entity in entities]);
	
	# Find table names of all declared entities
	classes  = [cls for cls in ada.entities.Base.__subclasses__()];
	declared = sorted([cls.__tablename__ for cls in classes]);
	
	# Prepare the list of the expected tables
	expected = [
		"Adjustments",
		"Candidates",
		"Corrections",
		"Deliveries",
		"Gatherings",
		"Items",
		"Logs",
		"Options",
		"Orders",
		"Payments",
		"Restaurants",
		"Summaries",
		"Transfers",
		"Users",
		"Votes",
		"Votings",
	];
	
	assert expected == declared;
	assert expected == defined;
	assert expected == created;

