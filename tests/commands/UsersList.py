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

def test(app, istrip, match):
	
	app.message(1,  'register user1');
	app.message(30, 'register user2');
	app.message(4,  'register user3');
	app.message(5,  'register user4');
#	app.message(2,  'delete <@4>');
	
	table = app.message("users-list");
	
	regex = istrip("""\
		\n```
		  Id    Did  Nick    Role        Created           Action
		----  -----  ------  ----------  ----------------  ----------------
		   1      1  user1   ROOT        [0123456789 :-]*  [0123456789 :-]*
		   2     30  user2   UNACCEPTED  [0123456789 :-]*  [0123456789 :-]*
		   3      4  user3   UNACCEPTED  [0123456789 :-]*  [0123456789 :-]*
		   4      5  user4   UNACCEPTED  [0123456789 :-]*  [0123456789 :-]*
		```""");
	
	assert match(regex, table);

