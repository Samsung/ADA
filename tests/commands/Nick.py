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
	
	app.message(1, "register nick1");
	app.message(2, "register nick2");
	app.message(1, "accept <@2>");
	app.message(1, 'nick nick3');
	
	assert raises(ValueError, r'This nick is incorrect, it',   app.message, 2, 'nick nick#');
	assert raises(ValueError, r'Old nick and new nick have',   app.message, 2, 'nick nick2');
	assert raises(ValueError, r'This nick is already in use!', app.message, 2, 'nick nick3');
	
	logs  = app.database.repos.logs.get_all();
	users = app.database.repos.users.get_all();
	
	assert len(logs)  == 7;
	assert len(users) == 2;
	assert equal(users[0], "User(id=1, did=1, nick=nick3, role=50, log_created=1, log_action=4, log_role=1)");
	assert equal(users[1], "User(id=2, did=2, nick=nick2, role=20, log_created=2, log_action=7, log_role=3)");

