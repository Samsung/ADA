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

def test(app, match, raises):
	
	app.message("register user");
	app.message("rest-add rest");
	app.message("start");
	app.message("cancel");
	app.message("start");
	app.message("submit rest");
	app.message("next");
	app.message("cancel");
	app.message("start rest");
	app.message("cancel");
	
	deliveries = app.database.repos.deliveries.get_all();
	
	assert len(deliveries) == 3;
	assert match(r"Delivery\(id=1, started=202.*, stage=Stage.GATHER, ignored=True, ended=202.*, log_start=3, log_end=4\)", deliveries[0]);
	assert match(r"Delivery\(id=2, started=202.*, stage=Stage.VOTE, ignored=True, ended=202.*, log_start=5, log_end=8\)",   deliveries[1]);
	assert match(r"Delivery\(id=3, started=202.*, stage=Stage.ORDER, ignored=True, ended=202.*, log_start=9, log_end=10\)", deliveries[2]);

