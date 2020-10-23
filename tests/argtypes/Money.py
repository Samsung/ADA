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

import ada;
from argparse import ArgumentTypeError;

def execute_range_test(app, start, stop, step):
	
	for value in range(start, stop, step):
		value_str = app.argtypes.money.format(value);
		value_int = app.argtypes.money(value_str);
		assert value_int == value;
	
	stop_str = app.argtypes.money.format(stop);
	stop_int = app.argtypes.money(stop_str);
	assert stop_int == stop;

def test_automatic(app):
	
	VALUE_MIN   = ada.argtypes.Money.VALUE_MIN;
	VALUE_MAX   = ada.argtypes.Money.VALUE_MAX;
	VALUE_RANGE = VALUE_MAX - VALUE_MIN;
	VALUE_STEP  = int(VALUE_RANGE**0.5);
	
	execute_range_test(app, -VALUE_STEP, VALUE_STEP, 1);
	execute_range_test(app, VALUE_MIN, VALUE_MIN+VALUE_STEP, 1);
	execute_range_test(app, VALUE_MAX-VALUE_STEP, VALUE_MAX, 1);
	execute_range_test(app, VALUE_MIN, VALUE_MAX, VALUE_STEP);

def test_zero(app, raises):
	
	assert app.argtypes.money("0")    == 0;
	assert app.argtypes.money("+0")   == 0;
	assert app.argtypes.money("-0")   == 0;
	assert app.argtypes.money("0.0")  == 0;
	assert app.argtypes.money("0.00") == 0;
	
	assert raises(ArgumentTypeError, "has to match to this input filter", app.argtypes.money, ".0");
	assert raises(ArgumentTypeError, "has to match to this input filter", app.argtypes.money, "00");
	assert raises(ArgumentTypeError, "has to match to this input filter", app.argtypes.money, "01");
	assert raises(ArgumentTypeError, "has to match to this input filter", app.argtypes.money, "00.");
	assert raises(ArgumentTypeError, "has to match to this input filter", app.argtypes.money, "00.0");
	assert raises(ArgumentTypeError, "has to match to this input filter", app.argtypes.money, "0.000");

def test_values(app, raises):
	
	assert app.argtypes.money(       "0.01") ==          1;
	assert app.argtypes.money(      "-0.01") ==         -1;
	assert app.argtypes.money(       "0.50") ==         50;
	assert app.argtypes.money(      "-0.50") ==        -50;
	assert app.argtypes.money(       "1.00") ==        100;
	assert app.argtypes.money(      "-1.00") ==       -100;
	assert app.argtypes.money(   "12345.67") ==    1234567;
	assert app.argtypes.money(  "-12345.67") ==   -1234567;
	assert app.argtypes.money( "1000000.00") ==  100000000;
	assert app.argtypes.money("-1000000.00") == -100000000;
	
	assert raises(ArgumentTypeError, "has to match to this input filter", app.argtypes.money, "1 2");
	assert raises(ArgumentTypeError, "has to match to this input filter", app.argtypes.money, "12+");
	assert raises(ArgumentTypeError, "has to match to this input filter", app.argtypes.money, "12-");
	assert raises(ArgumentTypeError, "has to match to this input filter", app.argtypes.money, "12.");
	assert raises(ArgumentTypeError, "has to match to this input filter", app.argtypes.money, "1..2");
	assert raises(ArgumentTypeError, "has to match to this input filter", app.argtypes.money, "1234.567");
	assert raises(ArgumentTypeError, "has to match to this input filter", app.argtypes.money, "01234");
	assert raises(ArgumentTypeError, "has to match to this input filter", app.argtypes.money, "01234.00");
	assert raises(ArgumentTypeError, "Money only supports values from",   app.argtypes.money, "1000001");
	assert raises(ArgumentTypeError, "Money only supports values from",   app.argtypes.money, "-1000001");
	assert raises(ArgumentTypeError, "Money only supports values from",   app.argtypes.money, "1000000.01");
	assert raises(ArgumentTypeError, "Money only supports values from",   app.argtypes.money, "-1000000.01");

def test_calculations(app, raises):
	
	assert app.argtypes.money(   "1 + 2 + 3 + 4") == 1000;
	assert app.argtypes.money(  "-1 + 2 - 3 + 4") ==  200;
	assert app.argtypes.money(  "1 + 0.2 + 0.03") ==  123;
	assert app.argtypes.money("1+0.5-11.11+0.02") == -959;
	
	assert raises(ArgumentTypeError, "has to match to this input filter",   app.argtypes.money, "1 + +2");
	assert raises(ArgumentTypeError, "has to match to this input filter",   app.argtypes.money, "1 + -2");

def test_str(app, raises):
	
	assert app.argtypes.money.format(         0) ==        "0.00";
	assert app.argtypes.money.format(         1) ==        "0.01";
	assert app.argtypes.money.format(        -1) ==       "-0.01";
	assert app.argtypes.money.format(        12) ==        "0.12";
	assert app.argtypes.money.format(       -12) ==       "-0.12";
	assert app.argtypes.money.format(      1234) ==       "12.34";
	assert app.argtypes.money.format( 100000000) ==  "1000000.00";
	assert app.argtypes.money.format(-100000000) == "-1000000.00";
	
	assert raises(ArgumentTypeError, "MoneyType only supports values from", app.argtypes.money.format,  100000001);
	assert raises(ArgumentTypeError, "MoneyType only supports values from", app.argtypes.money.format, -100000001);

