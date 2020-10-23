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
	app.message(4, "register user4");
	app.message(5, "register user5");
	app.message(6, "register user6");
	app.message(7, "register user7");
	app.message(8, "register user8");
	app.message(9, "register user9");
	
	app.message(1, "role <@2> ADMIN");
	app.message(2, "role <@3> MODERATOR");
	app.message(2, "role <@4> REGULAR");
	app.message(2, "role <@5> UNACCEPTED");
	app.message(2, "role <@6> BANNED");
	app.message(2, "role <@7> SETTLEMENT");
	app.message(2, "role <@8> SETTLEMENT"); # TODO: THIS ROLE SHOULD BE "DELETED"
	
	assert raises(Exception, "Access denied: at least ADMIN role is required!", app.message, 3, "role <@9> REGULAR");
	assert raises(Exception, "The ROOT role cannot be pick up directly!",       app.message, 2, "role <@1> ADMIN");
	assert raises(Exception, "The ROOT role cannot be changed directly!",       app.message, 2, "role <@2> ROOT");
	assert raises(KeyError,  "Role XXX does not exists!",                       app.message, 2, "role <@9> XXX");
	
	logs  = app.database.repos.logs.get_all();
	users = app.database.repos.users.get_all();
	
	assert len(logs)  == 20;
	assert len(users) ==  9;
	assert equal(users[0], "User(id=1, did=1, nick=user1, role=50, log_created=1, log_action=10, log_role=1)");
	assert equal(users[1], "User(id=2, did=2, nick=user2, role=40, log_created=2, log_action=20, log_role=10)");
	assert equal(users[2], "User(id=3, did=3, nick=user3, role=30, log_created=3, log_action=17, log_role=11)");
	assert equal(users[3], "User(id=4, did=4, nick=user4, role=20, log_created=4, log_action=4, log_role=12)");
	assert equal(users[4], "User(id=5, did=5, nick=user5, role=10, log_created=5, log_action=5, log_role=13)");
	assert equal(users[5], "User(id=6, did=6, nick=user6, role=-10, log_created=6, log_action=6, log_role=14)");
	assert equal(users[6], "User(id=7, did=7, nick=user7, role=-20, log_created=7, log_action=7, log_role=15)");
#	assert equal(users[7], "User(id=8, did=8, nick=user8, role=-30, log_created=8, log_action=8, log_role=16)"); # TODO
	assert equal(users[8], "User(id=9, did=9, nick=user9, role=10, log_created=9, log_action=9, log_role=9)");

