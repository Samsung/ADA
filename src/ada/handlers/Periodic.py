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

from .Base import *;

import ada;
import logging;
import discord;
import asyncio;
import datetime;

class Periodic(Base):
	"""Class for handling timeout events.
	"""
	
	def __call__(self):
		pass;
	
	def autostart(self):
		
		now      = datetime.datetime.now();
		delivery = ada.database.Delivery.getCurrent();
		# TODO
	
	def timeout(self):
		
		timeout  = None;
		now      = datetime.datetime.now();
		delivery = ada.database.Delivery.getCurrent();
		stage    = ada.database.Delivery.getStage(delivery);
		service  = ada.Services.getByStage(stage);
		
		if   stage == ada.core.Stages.GATHER:
			timeout = delivery.re_gathering.timeout;
		elif stage == ada.core.Stages.VOTE:
			timeout = delivery.re_gathering.re_voting.timeout;
		elif stage == ada.core.Stages.ORDER:
			timeout = delivery.re_gathering.re_voting.re_order.timeout;
		
		if not timeout:
			return;
		
		if timeout < now:
			return;
		
		try:
			msg = service.next();
			msg = 'Timeout!!!\n{}'.format(msg);
			self.app.loop.response(self.app.args.channel, msg);
		except:
			pass;

