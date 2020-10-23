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

def test(app):
	
	app.message('register user');
	app.message('rest-add rest');
	app.message('status');
	app.message('start');
	app.message('status');
	app.message('submit rest');
	app.message('status');
	app.message('next');
	app.message('status');
	app.message('vote 1');
	app.message('status');
	app.message('next');
	app.message('status');
	app.message('order 10.00 item');
	app.message('status');
	app.message('next');
	app.message('status');
	app.message('price 11.00 15:00');
	app.message('status');
	app.message('next');
	app.message('status');
	app.message('correct <@1> 1.00 correct');
	app.message('status');
	app.message('finish');
	app.message('status');

