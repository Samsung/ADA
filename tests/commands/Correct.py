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

def test(app, raises, equal):
	
	app.message(11, "register user1");
	app.message(22, "register user2");
	app.message(33, "register user3");
	app.message(11, "role <@22> MODERATOR");
	app.message(11, "role <@33> REGULAR");
	app.message(11, "rest-add rest");
	app.message(11, "start rest");
	app.message(11, "order 10.00 item1");
	app.message(22, "order 10.00 item2");
	app.message(11, "next");
	app.message(11, "price 25.00");
	app.message(11, "next");
	app.message(22, "correct <@22>   5.00 korekta");
	app.message(22, "correct <@11>  10.00 następna korekta");
	app.message(11, "correct <@11> -10.00 cofnięcie korekty");
	
	assert raises(Exception, "following arguments are required: note", app.message, 11, "correct <@11> 1.00");
	assert raises(Exception, "Money value has to match to .* filter",  app.message, 11, "correct <@11> aaaa bbbb");
	assert raises(Exception, "Invalid user mention string",            app.message, 11, "correct @xxxx 1.00 bbbb");
	
	delivery    = app.database.repos.deliveries.get_current();
	corrections = delivery.re_gathering.re_voting.re_order.re_summary.re_adjustment.re_corrections;
	
	assert len(corrections) == 3;
	assert equal(corrections[0], "Correction(id=1, adjustment=1, corrector=2, purchaser=2, price=500, note=korekta, log=13)");
	assert equal(corrections[1], "Correction(id=2, adjustment=1, corrector=2, purchaser=1, price=1000, note=następna korekta, log=14)");
	assert equal(corrections[2], "Correction(id=3, adjustment=1, corrector=1, purchaser=1, price=-1000, note=cofnięcie korekty, log=15)");

