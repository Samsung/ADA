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

def test_memory():
	
	# Create and initialize database object
	database = ada.core.Database(
		base_ents  = ada.entities.Base,
		base_repos = ada.repositories.Base,
	);
	
	# Create and save into database new log
	new_log = ada.entities.Log(None, 1, 2, None, "Test", 1, None);
	database.session.add(new_log);
	database.session.commit();
	
	# Get previously created log
	logs = database.repos.logs.get_all();
	
	# Check if it is correct log object
	assert len(logs)       == 1;
	assert logs[0].id      == 1;
	assert logs[0].content == "Test";

def test_file(tmp_path):
	
	# Prepare path to temporary database file
	file_name = "database.sqlite";
	file_path = tmp_path.joinpath(file_name);
	
	# Create and initialize database object
	database = ada.core.Database(
		base_ents  = ada.entities.Base,
		base_repos = ada.repositories.Base,
		file       = file_path,
	);
	
	# Create testing entry into database
	new_log = ada.entities.Log(None, 1, 2, None, "Test", 1, None);
	database.session.add(new_log);
	database.session.commit();
	
	# Close database session
	database.session.close();
	
	# Create new database session object
	database_new = ada.core.Database(
		base_ents  = ada.entities.Base,
		base_repos = ada.repositories.Base,
		file       = file_path,
	);
	
	# Select testing entity from database
	logs = database.repos.logs.get_all();
	
	# Check if it is correct log object
	assert len(logs)       == 1;
	assert logs[0].id      == 1;
	assert logs[0].content == "Test";

