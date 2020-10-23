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

def test(app, equal):
	
	app.message("register user");
	
	app.message("rest-add keyA nameA urlA");
	app.message("rest-add keyB nameB urlB");
	app.message("rest-add keyC nameC urlC");
	app.message("rest-add keyD nameD urlD");
	
	app.message("rest-set keyA key    keyX");
	app.message("rest-set keyB name   nameX");
	app.message("rest-set keyC url    urlX");
	app.message("rest-set keyD active 0");
	
	logs  = app.database.repos.logs.get_all();
	rests = app.database.repos.restaurants.get_all();
	
	assert len(logs)  == 9;
	assert len(rests) == 4;
	assert equal(rests[0], "Restaurant(id=1, key=keyX, name=nameA, url=urlA, active=True, log_created=2, log_action=2)");
	assert equal(rests[1], "Restaurant(id=2, key=keyB, name=nameX, url=urlB, active=True, log_created=3, log_action=3)");
	assert equal(rests[2], "Restaurant(id=3, key=keyC, name=nameC, url=urlX, active=True, log_created=4, log_action=4)");
	assert equal(rests[3], "Restaurant(id=4, key=keyD, name=nameD, url=urlD, active=False, log_created=5, log_action=5)");

