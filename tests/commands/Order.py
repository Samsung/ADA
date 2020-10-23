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
	app.message("accept <@2>");
	app.message("accept <@3>");
	app.message("rest-add rest");
	app.message("start rest");
	app.message(2, "order 30.00 jakieś zamówienie");
	app.message(3, "order 20.00 kolejne zamówienie");
	app.message(2, "order 35.55 inne zamówienie");
	
	assert raises(Exception, ".*", app.message, "order 10.00");
	assert raises(Exception, ".*", app.message, "order -10.00 zamówienie");
	assert raises(Exception, ".*", app.message, "order aaa zamówienie");
	assert raises(Exception, ".*", app.message, "order 0.0000000001 zamówienie");
	
	delivery = app.database.repos.deliveries.get_current();
	items    = delivery.re_gathering.re_voting.re_order.re_items;
	
	assert len(items) == 2;
	assert equal(items[0], "Item(id=1, order=1, purchaser=2, price=3555, note=inne zamówienie, log=10)");
	assert equal(items[1], "Item(id=2, order=1, purchaser=3, price=2000, note=kolejne zamówienie, log=9)");

