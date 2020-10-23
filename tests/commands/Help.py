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

def test(app, istrip):
	
	help = app.message("help");
	
	assert help == istrip("""
		```
		Ada (Automatic Delivery Aid) - discord bot for ordering food
		
		For more details type command: help COMMAND_NAME
		
		Commands specific for this stage: 
		
		Table of commands:
		Name        Role       Help
		----------  ---------  ----------------------------------------------------------------------
		accept      MODERATOR  Accept user account.
		back        MODERATOR  Go to previous delivery stage. (not implemented)
		balance     REGULAR    Print all accounts balance.
		cancel      MODERATOR  Cancel current delivery.
		correct     REGULAR    Create correction for current delivery.
		etofa       REGULAR    Set estimated time of arrival for current delivery.
		finish      MODERATOR  Finish current delivery.
		help        NONE       Show help information about commands.
		history     REGULAR    Print history of your balance.
		next        MODERATOR  Go to next delivery stage.
		nick        REGULAR    Change your nickname.
		order       REGULAR    Create or update order item for current delivery.
		orderr      REGULAR    Create or update order item for current delivery (reversed arguments).
		price       REGULAR    Save information about delivery price.
		register    NONE       Create a new user account.
		reject      MODERATOR  Reject restaurant voting candidate for current delivery.
		rest-add    MODERATOR  Add new restaurant to restaurant list.
		rest-del    ADMIN      Delete restaurant from restaurant list.
		rest-list   REGULAR    Show the list of restaurants.
		rest-set    ADMIN      Change information in restaurant list.
		role        ADMIN      Change privileges, accept, ban and delete users accounts.
		sleep       ADMIN      Got to sleep for few seconds.
		start       MODERATOR  Start new delivery process.
		status      REGULAR    Get status of current delivery.
		submit      REGULAR    Submit restaurant voting candidate for current delivery.
		users-list  REGULAR    List all registered users.
		vote        REGULAR    Vote for the candidates in VOTE stage.
		```
		""");

def test_correct(app, istrip):
	
	help = app.message("help correct");
	
	assert help == istrip("""
		```
		Name: correct
		Role: REGULAR
		Stages: ADJUST
		Args: user price note [note ...]
		
		Create correction for current delivery.
		
		positional arguments:
		  user   Mention of the user related to the correction.
		  price  Amount of the correction, it has to be in the money or simple
		         calculation format, examples: 1, 2.50, 4+2-0.50.
		  note   Note with the description of the correction.
		
		```
		""");

def test_not_found(app, raises):
	
	assert raises(KeyError, "Command name not found!", app.message, "help xxx");

