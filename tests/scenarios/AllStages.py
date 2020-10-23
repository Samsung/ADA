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
	app.message(3, "register user3");
	app.message(4, "register user4");
	app.message(5, "register user5");
	app.message(6, "register user6");
	
	app.message("accept <@2>");
	app.message("accept <@3>");
	app.message("accept <@4>");
	app.message("accept <@5>");
	app.message("accept <@6>");
	
	app.message("rest-add rest1");
	app.message("rest-add rest2");
	app.message("rest-add rest3");
	app.message("rest-add rest4");
	app.message("rest-add rest5");
	app.message("rest-add rest6");
	
	app.message("start");
	
	app.message("submit rest2");
	app.message("submit rest5 rest3");
	
	app.message("next");
	
	app.message(3, "vote  1  2  3");
	app.message(2, "vote  4  5  6");
	app.message(1, "vote  7  8  9");
	app.message(4, "vote  0  0  5");
	app.message(3, "vote 10  0  0");
	
	app.message("next");
	
	app.message(2, "order 10.00 Zamówienie nr 1");
	app.message(3, "order 20.00 Zamówienie nr 2");
	app.message(1, "order 30.00 Zamówienie nr 3");
	app.message(2, "order 40.00 Zamówienie nr 4");
	app.message(4, "order 50.00 Zamówienie nr 5");
	
	app.message("next");
	
	app.message("price 140.00 14:00");
	app.message("etofa 14:30");
	app.message("price 160.00");
	
	app.message("next");
	
	app.message("correct <@2> 25.00 korekta");
	app.message("correct <@3> -5.00 korekta");
	
	app.message("finish");
	
	balance = app.message("balance");
	
	assert balance == istrip("""\
		```
		User      Total
		------  -------
		user1    130.00
		user2    -65.00
		user3    -15.00
		user4    -50.00
		user5      0.00
		user6      0.00
		Total      0.00
		```""");

