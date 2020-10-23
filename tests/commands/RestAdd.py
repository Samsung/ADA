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
	app.message("rest-add keyB nameB");
	app.message("rest-add keyC nameC urlC");
	
	assert raises(ValueError, r"^Restaurant with key keyA already exists!$",   app.message, "rest-add keyA nameD urlD");
	assert raises(ValueError, r"^Restaurant with name nameB already exists!$", app.message, "rest-add keyE nameB urlE");
	assert raises(ValueError, r"^Restaurant with URL urlC already exists!$",   app.message, "rest-add keyF nameF urlC");
	
	logs  = app.database.repos.logs.get_all();
	rests = app.database.repos.restaurants.get_all();
	
	assert len(logs)  == 7;
	assert len(rests) == 3;
	assert equal(rests[0], "Restaurant(id=1, key=keyA, name=keyA, url=None, active=True, log_created=2, log_action=2)");
	assert equal(rests[1], "Restaurant(id=2, key=keyB, name=nameB, url=None, active=True, log_created=3, log_action=3)");
	assert equal(rests[2], "Restaurant(id=3, key=keyC, name=nameC, url=urlC, active=True, log_created=4, log_action=4)");

