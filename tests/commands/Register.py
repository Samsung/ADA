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
	
	app.message(1, "register user1");
	app.message(2, "register user2");
	app.message(3, "register user3");
	
	assert raises(ValueError, r"^This nick is incorrect",       app.message, 4, "register nick$");
	assert raises(ValueError, r"^Discord id 3 already exists!", app.message, 3, "register user4");
	assert raises(ValueError, r"^Nick user3 already exists!",   app.message, 5, "register user3");
	
	logs  = app.database.repos.logs.get_all();
	users = app.database.repos.users.get_all();
	
	assert len(logs)  == 6;
	assert len(users) == 3;
	assert equal(users[0], "User(id=1, did=1, nick=user1, role=50, log_created=1, log_action=1, log_role=1)");
	assert equal(users[1], "User(id=2, did=2, nick=user2, role=10, log_created=2, log_action=2, log_role=2)");
	assert equal(users[2], "User(id=3, did=3, nick=user3, role=10, log_created=3, log_action=5, log_role=3)");

