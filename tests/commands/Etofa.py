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

def test(app, raises, match):
	
	app.message('register user');
	app.message('rest-add rest');
	app.message('start rest');
	app.message('order 1.00 item');
	app.message('next');
	app.message('etofa 14:00');
	app.message('etofa 15:00');
	
	assert raises(Exception, '.*',    app.message, 'etofa AAAAA');
	assert raises(Exception, '.*',    app.message, 'price 0A:00');
	assert raises(Exception, '.*',    app.message, 'price 00:B0');
	assert raises(Exception, '.*',    app.message, 'price 15:001');
	assert raises(Exception, '.*',    app.message, 'price 111:00');
	
	delivery = app.database.repos.deliveries.get_current();
	payment  = delivery.re_gathering.re_voting.re_order.re_summary.re_payment;
	
	assert match(r"Payment\(id=1, payer=None, price=None, etofa=.*15:00:00, log=None\)", payment);

