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

class Delivery(Base):
	
	def start(self,
			log        : ada.entities.Log,
			restaurant : ada.entities.Restaurant = None)\
			-> ada.entities.Delivery:
		
		if self.database.repos.deliveries.get_current():
			msg = 'Delivery process is already started.';
			raise Exception(msg);
		
		timeout   = None; # ada.core.Config.timeout('GATHER');
		started   = datetime.datetime.now();
		stage     = ada.entities.Stage.GATHER;
		delivery  = ada.entities.Delivery(started, stage, log_start=log);
		gathering = ada.entities.Gathering(delivery, timeout=timeout);
		self.database.session.add(delivery);
		self.database.session.add(gathering);
		
		# If restaurant was given, then start ordering
		if restaurant:
			self.services.gathering.submit(gathering, restaurant, log);
			self.services.gathering.next();
			self.services.voting.next();
		
		return delivery;
	
	def cancel(self, log):
		
		# Get current delivery
		delivery   = self.repos.deliveries.get_current();
		
		# Change delivery stage
		delivery.ended      = datetime.datetime.now();
		delivery.ignored    = True;
		delivery.re_log_end = log;
		
		# Save delivery stage
		self.database.session.commit();
		
		return delivery;
	
	def finish(self, log):
		
		# Get necessary information from current delivery
		delivery   = self.repos.deliveries.get_current();
		order      = delivery.re_gathering.re_voting.re_order;
		summary    = order.re_summary;
		adjustment = summary.re_adjustment;
		
		# Get all objects containing price information
		items       = order.re_items;
		payment     = summary.re_payment;
		corrections = adjustment.re_corrections;
		
		# Variable to storage delivery balance
		balance = self.repos.deliveries.get_balance(delivery);
		
		# Test if delivery can be ended
		if abs(balance) > 0:
			msg = 'Before finishing delivery, balance have to be zero, but now it is {:0.2f}.';
			msg = msg.format(balance);
			raise Exception(msg);
		
		# Change delivery stage
		delivery.stage      = ada.entities.Stage.FINISH;
		delivery.ended      = datetime.datetime.now();
		delivery.ignored    = False;
		delivery.re_log_end = log;
		
		# Save delivery stage
		self.database.session.commit();
		
		# Return finished delivery
		return delivery;

