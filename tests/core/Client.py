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
import os;
import pytest;

class Handlers:
	
	def __init__(self):
		self.c_ready    = 0;
		self.c_periodic = 0;
		self.c_finish   = 0;
		self.c_message  = 0;
		self.c_format   = 0;
		self.c_step     = 0;
		self.client     = None;
	
	def ready(self):
		self.c_ready += 1;
		self.c_step  += 1;
		return "ADA:UnitTest:ready";
	
	def periodic(self):
		self.c_periodic += 1;
		self.c_step     += 1;
		self.client.on_finish();
		return "ADA:UnitTest:periodic";
	
	def finish(self):
		self.c_finish += 1;
		self.c_step   += 1;
		return "ADA:UnitTest:finish";
	
	def message(self, whoami, author, channel, content):
		self.c_message += 1;
		self.c_step    += 1;
		return "ADA:UnitTest:message";
	
	def format(self, content):
		self.c_format += 1;
		self.c_step   += 1;
		return [content];

@pytest.mark.skip
#@pytest.mark.asyncio
def test(event_loop):
	
	channel = os.getenv("ADA_PYTEST_CHANNEL");
	token   = os.getenv("ADA_PYTEST_TOKEN");
	
	if not channel or not token:
		pytest.skip("Some of the environment variables that are required for"\
		            " discord client test does not exists (ADA_PYTEST_CHANNEL"\
		            " or ADA_PYTEST_TOKEN).");
	
	handlers = Handlers();
	
	# Create discord client object
	client = ada.core.Client(
		handler_ready    = handlers.ready,
		handler_periodic = handlers.periodic,
		handler_finish   = handlers.finish,
		handler_message  = handlers.message,
		handler_format   = handlers.format,
		conf_channel     = channel,
		conf_delay       = 1.0,
		conf_loopback    = False, # True,
	);
	
	# Save client object into handlers
	handlers.client = client;
	
	# Run discord client
	client.run(token);

