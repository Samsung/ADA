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

def test(app, istrip):
	
	app.message(1, "register user1");
	app.message(2, "register user2");
	app.message("accept <@2>");
	app.message("rest-add rest");
	
	app.message("start rest");
	app.message("order 10.0 coś");
	app.message("order 10.0 coś2");
	app.message("next");
	app.message("price 12.00");
	app.message("next");
	app.message("correct <@1> 1.00 correct1");
	app.message("correct <@2> 1.00 correct2");
	app.message("finish");
	
	app.message("start rest");
	app.message("order 9.0 coś");
	app.message("next");
	app.message("price 20.00");
	app.message("next");
	app.message("correct <@1>  1.00 correct1");
	app.message("cancel");
	
	app.message("start rest");
	app.message(1, "order 12 coś");
	app.message(2, "order 14 coś2");
	app.message("next");
	app.message(2, "price 30.00");
	app.message("next");
	app.message("correct <@1> 4.00 correct1");
	app.message("finish");
	
	balance = app.message("balance");
	
	assert balance == istrip("""\
		```
		User      Total
		------  -------
		user1    -15.00
		user2     15.00
		Total      0.00
		```""");

