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

class Items(Base):
	"""
		Repository class for Item entity.
	"""
	
	entity = entities.Item;
	
	def create_or_update(self,
			order     : ada.entities.Order,
			purchaser : ada.entities.User,
			price     : int,
			note      : str,
			log       : ada.entities.Log):
		
		# Try to find previous order item.
		item = self.get_one(re_order = order, re_purchaser = purchaser);
		
		# If order item does not exists, then create it
		if item is None:
			item = ada.entities.Item(order, purchaser);
			self.session.add(item);
		
		# Update order item values
		item.price  = price;
		item.note   = note;
		item.re_log = log;
		
		return item;

