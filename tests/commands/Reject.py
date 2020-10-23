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


def test(app, equal):
	
	app.message("register user");
	app.message("rest-add rest1");
	app.message("rest-add rest2");
	app.message("rest-add rest3");
	app.message("rest-add rest4");
	app.message("start");
	app.message("submit rest1 rest3");
	app.message("submit rest2 rest4");
	app.message("reject rest1 rest4");
	
	delivery   = app.database.repos.deliveries.get_current();
	candidates = delivery.re_gathering.re_candidates;
	
	assert len(candidates) == 2;
	assert equal(candidates[0], "Candidate(id=3, gathering=1, restaurant=2, log=8)");
	assert equal(candidates[1], "Candidate(id=2, gathering=1, restaurant=3, log=7)");

