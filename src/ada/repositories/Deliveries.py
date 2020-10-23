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

class Deliveries(Base):
	"""
		Repository class for Delivery entity.
	"""
	
	entity = entities.Delivery;
	
	def get_balance(self, delivery):
		
		# Get necessary information from current delivery
		order      = delivery.re_gathering.re_voting.re_order;
		summary    = order.re_summary;
		adjustment = summary.re_adjustment;
		
		# Auxiliary variables
		item  = ada.entities.Item;
		corr  = ada.entities.Correction;
		query = self.session.query;
		
		# Get delivery balance components
		balance_items    = query(func.sum(item.price)).filter(item.re_order      == order     ).scalar();
		balance_payment  = summary.re_payment.price;
		balance_corrects = query(func.sum(corr.price)).filter(corr.re_adjustment == adjustment).scalar();
		
		# Make sure, that every component has numeric value
		balance_items    = balance_items    or 0;
		balance_payment  = balance_payment  or 0;
		balance_corrects = balance_corrects or 0;
		
		# Add components of the delivery balance
		balance = -balance_items + balance_payment - balance_corrects;
		
		# Return delivery balance
		return balance;
	
	def get_current(self, id=False):
		
		try:
			
			# Try to find current delivery
			query  = self.query();
			query  = query.filter(self.entity.ended == None);
			query  = query.filter(self.entity.ignored == False);
			result = query.order_by(self.entity.id).one_or_none();
			
			# If current delivery don't exists return None
			if result is None:
				return None;
			
			# Otherwise return delivery object or id
			if id:
				return result.id;
			else:
				return result;
			
		except Exception as e:
			print(e)
			# Throw exception in case of error
			msg = 'Error while searching for current deliver.';
			raise Exception(msg) from e;
	
	def get_stage(self, delivery=None):
		try:
			if delivery is None:
				delivery = self.get_current();
			
			if delivery is None:
				return ada.entities.Stage.SLEEP;
			
			return delivery.stage;
		except Exception as e:
			# Throw exception in case of error
			msg = 'Error while getting stage.';
			raise Exception(msg) from e;

