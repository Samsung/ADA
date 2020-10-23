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

def test_default(app):
	
	app.message("register user");
	app.message("rest-add rest_a 'Rest A' https://rest_a/");
	app.message("start");
	app.message("submit rest_a");
	app.message("next");
	status = app.message("next");
	
	assert "Rest A (`https://rest_a/`)" in status;

def test_none(app):
	
	app.message("register user");
	app.message("rest-add rest");
	app.message("start");
	app.message("submit rest");
	app.message("next");
	status = app.message("next");
	
	assert "rest (`None`)" in status;

