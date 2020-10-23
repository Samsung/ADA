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

def test(app, raises, equal):
	
	app.message("register user");
	app.message("rest-add keyA");
	app.message("rest-add keyB");
	app.message("rest-del keyA");
	
	assert raises(ValueError, r"^Restaurant with key keyA does not exists!$",   app.message, "rest-del keyA");
	assert raises(ValueError, r"^Restaurant with key keyC does not exists!$",   app.message, "rest-del keyC");
	
	logs  = app.database.repos.logs.get_all();
	rests = app.database.repos.restaurants.get_all();
	
	assert len(logs)  == 6;
	assert len(rests) == 1;
	assert equal(rests[0], "Restaurant(id=2, key=keyB, name=keyB, url=None, active=True, log_created=3, log_action=3)");




"""

def test(app, raises, equal):
	
	app.message("register user");
	app.message("rest-add keyA");
	app.message("rest-add keyB");
	app.message("rest-add keyC");
	app.message("rest-del keyB");
	app.message("start keyC");
	
	assert raises(ValueError, r"^Restaurant with key urlB does not exists!$",   app.message, "rest-del urlB");
	assert raises(ValueError, r"^Restaurant with key urlD does not exists!$",   app.message, "rest-del urlD");
	assert raises(ValueError, r"^The restaurant cannot be deleted, .*instead.", app.message, "rest-del keyC");
	
	logs  = app.database.repos.logs.get_all();
	rests = app.database.repos.restaurants.get_all();
	
	assert len(logs)  == 9;
	assert len(rests) == 2;
	assert equal(rests[0], "Restaurant(id=1, key=keyA, name=keyA, url=None, active=True, log_created=2, log_action=2)");
	assert equal(rests[1], "Restaurant(id=3, key=keyC, name=keyC, url=None, active=True, log_created=4, log_action=4)");
"""
