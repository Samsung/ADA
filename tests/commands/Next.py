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
import ada;

def test(app, raises):
	
####################################################################### Starting
	
	app.message("register root");
	app.message("rest-add rest");
	app.message("start");
	
###################################################################### Gathering
	
	delivery  = app.database.repos.deliveries.get_current();
	gathering = delivery.re_gathering;
	
	assert gathering is not None;
	assert delivery.stage == ada.entities.Stage.GATHER;
	assert raises(Exception, r"no candidates for voting", app.message, "next");
	
	app.message("submit rest");
	app.message("next");
	
######################################################################### Voting
	
	voting = gathering.re_voting;
	
	assert voting is not None;
	assert delivery.stage == ada.entities.Stage.VOTE;
	
	app.message("next");
	
####################################################################### Ordering
	
	wrest = voting.re_winner.re_restaurant;
	order = voting.re_order;
	
	assert wrest is not None;
	assert order is not None;
	assert wrest.name == "rest";
	assert delivery.stage == ada.entities.Stage.ORDER;
	assert raises(Exception, r"no items to order", app.message, "next");
	
	app.message("order 10.00 item");
	app.message("next");
	
######################################################################## Summary
	
	summary = order.re_summary;
	assert summary is not None;
	assert delivery.stage == ada.entities.Stage.SUMMARY;
	assert raises(Exception, "There is no payment!", app.message, "next");
	
	app.message("price 10.00");
	app.message("next");
	
##################################################################### Correction
	
	adjustment = summary.re_adjustment;
	assert adjustment is not None;
	assert delivery.stage == ada.entities.Stage.ADJUST;
	assert raises(Exception, "not permitted in stage", app.message, "next");

