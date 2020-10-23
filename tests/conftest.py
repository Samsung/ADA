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

def fixture_function(function):
	wrapper = lambda: function;
	wrapper.__name__ = function.__name__;
	wrapper = pytest.fixture(wrapper);
	return wrapper

pytest.fixture.function = fixture_function;

from fixtures.app      import app;
from fixtures.database import database;
from fixtures.equal    import equal;
from fixtures.handlers import handlers;
from fixtures.istrip   import istrip;
from fixtures.match    import match;
from fixtures.ni       import ni;
from fixtures.raises   import raises;

