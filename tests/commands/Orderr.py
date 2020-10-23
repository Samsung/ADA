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
	
	app.message("register user");
	app.message("rest-add rest");
	app.message("start rest");
	app.message("orderr jakieś zamówienie + coś 10.00+20");
	
	delivery = app.database.repos.deliveries.get_current();
	items    = delivery.re_gathering.re_voting.re_order.re_items;
	
	assert len(items) == 1;
	assert equal(items[0], "Item(id=1, order=1, purchaser=1, price=3000, note=jakieś zamówienie + coś, log=4)");

