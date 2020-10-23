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

class Summary(Base):
	"""
		Repository class for Gathering entity.
	"""
	
	def init(self):
		self.entity = ada.entities.Summary;
	
	def status(self):
		
		# Get necessary information from current delivery
		delivery = self.repos.deliveries.get_current();
		summary  = delivery.re_gathering.re_voting.re_order.re_summary;
		payment  = summary.re_payment;
		
		# Create default response
		response = 'There is no information about current summary.';
		
		# If there are information about summary, create detailed response
		if payment is not None:
			payer    = 'None' if payment.re_payer is None else payment.re_payer.nick;
			price    = float(payment.price)/100; #TODO: This is ugly format fix!
			response = 'Payer {}, price {}, etofa {}.';
			response = response.format(payer, price, payment.etofa);
		
		# Return a response
		return response;
	
	def payment(self,
			payer    : ada.entities.User,
			price    : int,
			etofa    : datetime.datetime,
			log      : ada.entities.Log):
		
		# If price is not given,
		# then payer does not exists
		if price == 0:
			user  = None;
			payer = None;
		
		# Validating price value
		if price < 0:
			msg = 'The price can not be negative!';
			raise ValueError(msg);
		elif price > 1000000:
			msg = 'The price is too high!';
			raise ValueError(msg);
		
		# Get or create payment object for current delivery
		delivery = self.repos.deliveries.get_current();
		summary  = delivery.re_gathering.re_voting.re_order.re_summary;
		payment  = self.repos.payments.get_or_create(summary);
		
		# Update payment object
		payment.re_payer = payer;
		payment.price    = price;
		payment.etofa    = etofa;
		payment.re_log   = log;
		
		# Save changes to database
		self.database.session.commit();
		
		# Return payment
		return payment;
	
	def etofa(self,
			etofa : datetime.datetime):
		
		# Get or create payment object for current delivery
		delivery = self.repos.deliveries.get_current();
		summary  = delivery.re_gathering.re_voting.re_order.re_summary;
		payment  = self.repos.payments.get_or_create(summary);
		
		# Change current etofa
		payment.etofa = etofa;
		
		# Save changes to database
		self.database.session.commit();
		
		# Return current payment
		return payment;
	
	def next(self):
		
		# Get necessary information from current delivery
		delivery = self.repos.deliveries.get_current();
		summary  = delivery.re_gathering.re_voting.re_order.re_summary;
		payment  = summary.re_payment;
		
		# Test if all necessary information are given
		if not payment:
			raise Exception('There is no payment!');
		if not payment.re_payer:
			raise Exception('There is no payer!');
		if not payment.price:
			raise Exception('There is no price!');
		if not payment.re_log:
			raise Exception('There is no log!');
		
		# Create new adjustment
		adjustment = ada.entities.Adjustment(summary);
		
		# Change delivery stage
		delivery.stage = ada.entities.Stage.ADJUST;
		
		# Commit all changes
		self.database.session.add(adjustment);
		self.database.session.commit();
		
		return '';

