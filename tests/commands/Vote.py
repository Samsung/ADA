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
	
	# Create users accounts
	app.message(1, "register user1");
	app.message(2, "register user2");
	app.message(3, "register user3");
	app.message(4, "register user4");
	app.message(5, "register user5");
	
	# Activate users accounts
	app.message("role <@2> REGULAR");
	app.message("role <@3> REGULAR");
	app.message("role <@4> REGULAR");
	app.message("role <@5> REGULAR");
	
	# Create some restaurants
	app.message("rest-add rest1");
	app.message("rest-add rest2");
	app.message("rest-add rest3");
	app.message("rest-add rest4");
	app.message("rest-add rest5");
	
	# Go through the gathering stage
	app.message("start");
	app.message("submit rest5 rest1");
	app.message("submit rest4");
	app.message("submit rest3");
	app.message("next");
	
	# Go through the voting stage
	app.message(1, "vote  1 2 3  4");
	app.message(3, "vote 10 9 8  7");
	app.message(2, "vote  5 5 5  5");
	app.message(1, "vote  0 0 0 10");

	assert raises(Exception, "candidates and the number of votes", app.message, "vote 1 2 3");
	assert raises(Exception, "candidates and the number of votes", app.message, "vote 1 2 3 4 5");
	assert raises(Exception, "argument vote: invalid int value",   app.message, "vote 0 0 0 b");
	assert raises(Exception, "argument vote: invalid int value",   app.message, "vote 0 0 0 1.5");
	assert raises(Exception, "argument vote: invalid choice",      app.message, "vote 0 0 0 -1");
	assert raises(Exception, "argument vote: invalid choice",      app.message, "vote 0 0 0 11");
	
	delivery = app.database.repos.deliveries.get_current();
	votes    = delivery.re_gathering.re_voting.re_votes;
	
	assert len(votes) == 12;
	assert equal(votes[ 0], "Vote(id=4, voting=1, voter=1, candidate=1, value=10, log=23)");
	assert equal(votes[ 1], "Vote(id=1, voting=1, voter=1, candidate=2, value=0, log=23)");
	assert equal(votes[ 2], "Vote(id=3, voting=1, voter=1, candidate=3, value=0, log=23)");
	assert equal(votes[ 3], "Vote(id=2, voting=1, voter=1, candidate=4, value=0, log=23)");
	assert equal(votes[ 4], "Vote(id=12, voting=1, voter=2, candidate=1, value=5, log=22)");
	assert equal(votes[ 5], "Vote(id=9, voting=1, voter=2, candidate=2, value=5, log=22)");
	assert equal(votes[ 6], "Vote(id=11, voting=1, voter=2, candidate=3, value=5, log=22)");
	assert equal(votes[ 7], "Vote(id=10, voting=1, voter=2, candidate=4, value=5, log=22)");
	assert equal(votes[ 8], "Vote(id=8, voting=1, voter=3, candidate=1, value=7, log=21)");
	assert equal(votes[ 9], "Vote(id=5, voting=1, voter=3, candidate=2, value=10, log=21)");
	assert equal(votes[10], "Vote(id=7, voting=1, voter=3, candidate=3, value=8, log=21)");
	assert equal(votes[11], "Vote(id=6, voting=1, voter=3, candidate=4, value=9, log=21)");

