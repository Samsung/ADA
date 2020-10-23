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

class Order(Base):
	
	def init(self):
		self.repo = self.database.repos.orders;
	
	def status(self):
		
		delivery = self.repos.deliveries.get_current();
		order    = delivery.re_gathering.re_voting.re_order;
		items    = order.re_items;
		
		# Create variables for table generating
		header = ['User',   'Price', 'Item'];
		footer = ['Total:',      '',     ''];
		rows   = list();
		total  = 0;
		
		# Generate table rows
		for item in items:
			user   = item.re_purchaser.nick;
			price  = float(item.price)/100; #TODO: This is ugly format fix!
			note   = item.note;
			total += price;
			rows.append([user, price, note]);
		
		# Add row with summary
		rows.append('');
		footer[1] = total;
		rows.append(footer);
		
		# Generate ascii table with results
		table = str(tabulate.tabulate(rows, header, tablefmt="simple"));
		table = "```\n{}\n```".format(table);
		
		# Return results table
		return table;
	
	def create_or_update_item(self,
			purchaser : ada.entities.User,
			price     : int,
			note      : str,
			log       : ada.entities.Log):
		
		if not note:
			msg = 'Order item description cannot be empty!';
			raise Exception(msg);
		
		if price < 0:
			msg = 'Order item price has to be positive!';
			raise ValueError(msg);
		
		if price > 500000:
			msg = "Order item price has to be less than 5000.00!";
			raise ValueError(msg);
		
		# Get order for current deliver
		delivery = self.repos.deliveries.get_current();
		order    = delivery.re_gathering.re_voting.re_order;
		
		# Create or update order item
		item = self.repos.items.create_or_update(order, purchaser, price, note, log);
		
		return item;
	
	def next(self):
		
		delivery = self.repos.deliveries.get_current();
		order    = delivery.re_gathering.re_voting.re_order;
		items    = order.re_items;
		
		if len(items) < 1:
			msg = 'There is no items to order.';
			raise Exception(msg);
		
		# Get voting status table
		table = self.status();
		
		# Change delivery stage
		delivery.stage = ada.entities.Stage.SUMMARY;
		
		# Create object for new stage
		summary = ada.entities.Summary(order);
		
		# Commit all changes
		self.database.session.add(summary);
		self.database.session.commit();
		
		# Return winner name
		return table;

