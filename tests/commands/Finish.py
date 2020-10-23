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
	
	app.message("register user");
	app.message("rest-add rest");
	app.message("start rest");
	app.message("order 1.00 item");
	app.message("next");
	app.message("price 2.00");
	app.message("next");
	
	assert raises(Exception, "balance have to be zero", app.message, "finish");
	
	app.message("correct <@1> 1.00 correction");
	app.message("finish");
	
	deliveries = app.database.repos.deliveries.get_all();
	
	assert len(deliveries) == 1;
	assert match(r"^Delivery\(id=1, started=202.*, stage=Stage.FINISH, ignored=False, "\
	                                r"ended=202.*, log_start=3, log_end=10\)$", deliveries[0]);

