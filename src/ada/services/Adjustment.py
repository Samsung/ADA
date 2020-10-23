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

class Adjustment(Base):
	
	def init(self):
		self.entity = ada.entities.Adjustment;
	
	def status(self):
		
		# Get necessary information from current delivery
		delivery   = self.repos.deliveries.get_current();
		order      = delivery.re_gathering.re_voting.re_order;
		summary    = order.re_summary;
		adjustment = summary.re_adjustment;
		
		# Get all objects containing price information
		items       = order.re_items;
		payment     = summary.re_payment;
		corrections = adjustment.re_corrections;
		
		# Create variables for table generating
		header = ['Type',   'Source', 'Amount', 'Description'];
		footer = [  None, 'Summary:',     None,          None];
		rows   = list();
		total  = 0.0;
		
		# Generate rows related to order items
		for item in items:
			total -= float(item.price);
			price = '{:0.2f}'.format(-float(item.price)/100); #TODO: This is ugly format fix!
			rows.append([
				'ITM',
				item.re_purchaser.nick,
				price,
				item.note,
			]);
		
		# Generate row related to summary payment
		total += float(payment.price);
		price = '{:0.2f}'.format(float(payment.price)/100); #TODO: This is ugly format fix!
		rows.append([
			'PAY',
			payment.re_payer.nick,
			price,
			None,
		]);
		
		# Generate rows related to order items
		for correction in corrections:
			total -= float(correction.price);
			price = '{:0.2f}'.format(-float(correction.price)/100); #TODO: This is ugly format fix!
			rows.append([
				'COR',
				correction.re_purchaser.nick,
				price,
				correction.note,
			]);
		
		# Add row with summary
		total = float(total)/100; #TODO: This is ugly format fix!
		footer[2] = '{:0.2f}'.format(total);
		rows.append('');
		rows.append(footer);
		
		# Generate ascii table with results
		table = str(tabulate.tabulate(rows, header, tablefmt="simple"));
		table = "```\n{}\n```".format(table);
		
		# Return results table
		return table;
	
	def correct(self, corrector, purchaser, price, note, log):
		
		# Get necessary information from current delivery
		delivery   = self.repos.deliveries.get_current();
		adjustment = delivery.re_gathering.re_voting.re_order.re_summary.re_adjustment;
		
		# Create object for new correction
		correction = ada.entities.Correction(adjustment, corrector, purchaser, price, note, log);
		
		# Save correction to database
		self.database.session.add(correction);
		self.database.session.commit();
		
		# Return success information
		return correction;

