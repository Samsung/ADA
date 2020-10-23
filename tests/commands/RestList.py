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

def test_default(app, istrip):
	
	app.message("register user");
	app.message("rest-add keyA");
	app.message("rest-add keyB nameB");
	app.message("rest-add keyC nameC urlC");
	
	table = app.message("rest-list");
	
	assert table == istrip("""\
		\n```
		  Id  Key    Name    Url    Active
		----  -----  ------  -----  --------
		   1  keyA   keyA           True
		   2  keyB   nameB          True
		   3  keyC   nameC   urlC   True
		```""");

def test_empty(app, istrip):
	
	app.message("register user");
	
	table = app.message("rest-list");
	
	assert table == istrip("""\
		\n```
		Id    Key    Name    Url    Active
		----  -----  ------  -----  --------
		```""");

