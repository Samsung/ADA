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
	
	history1 = app.message(1, "history");
	history2 = app.message(2, "history 2");
	
	regex1 = istrip("""\
		```
		Date                 Type      Amount    Delivery  Note
		-------------------  ------  --------  ----------  ----------------------
		[0123456789    :-]*  ITM          -10           1  coś2
		[0123456789    :-]*  PAY           12           1  Payment for delivery 1
		[0123456789    :-]*  COR           -1           1  correct1
		[0123456789    :-]*  ITM          -12           3  coś
		[0123456789    :-]*  COR           -4           3  correct1
		
		                     Total        -15
		```""");
	
	regex2 = istrip("""\
		```
		Date                 Type    Amount    Delivery    Note
		-------------------  ------  --------  ----------  ----------------------
		...                  ...     ...       ...
		[0123456789    :-]*  ITM     -14.00    3           coś2
		[0123456789    :-]*  PAY     30.00     3           Payment for delivery 3
		
		                     Total   15.00
		```""");
	
	assert match(regex1, history1);
	assert match(regex2, history2);

