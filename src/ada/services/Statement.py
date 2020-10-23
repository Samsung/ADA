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

class Statement(Base):
	
	def history(self,
			user   : ada.entities.User,
			length : int):
		
		headers = ["Date", "Type",  "Amount", "Delivery", "Note"];
		footer  = [None, "Total", None, None, None];
		rows    = list();
		
		items       = self.repos.items.get_all(purchaser=user.id);
		payments    = self.repos.payments.get_all(payer=user.id);
		corrections = self.repos.corrections.get_all(purchaser=user.id);
		sendeds     = self.repos.transfers.get_all(sender=user.id);
		receiveds   = self.repos.transfers.get_all(receiver=user.id);
		
		for item in items:
			delivery = item.re_order.re_voting.re_gathering.re_delivery;
			if delivery.ignored:
				continue;
			rows.append([
				item.re_log.date,
				"ITM",
				-item.price,
				delivery.id,
				item.note,
			]);
		
		for payment in payments:
			delivery = payment.re_summary.re_order.re_voting.re_gathering.re_delivery;
			if delivery.ignored:
				continue;
			rows.append([
				payment.re_log.date,
				"PAY",
				payment.price,
				delivery.id,
				"Payment for delivery {}".format(payment.id),
			]);
		
		for correct in corrections:
			delivery = correct.re_adjustment.re_summary.re_order.re_voting.re_gathering.re_delivery;
			if delivery.ignored:
				continue;
			rows.append([
				correct.re_log.date,
				"COR",
				-correct.price,
				delivery.id,
				correct.note,
			]);
		
		for send in sendeds:
			rows.append([
				send.re_log.date,
				"SEN",
				send.amount,
				None,
				send.note,
			]);
		
		for recv in receiveds:
			rows.append([
				recv.re_log.date,
				"REC",
				-recv.amount,
				None,
				recv.note,
			]);
		
		# Sort operations
		rows = sorted(rows, key=lambda row: row[0]);
		
		# Calculate amount balance
		total = sum([row[2] for row in rows]);
		
		# Cut off operations by limit
		if len(rows) > length:
			rows = rows[-length:];
			rows.insert(0, ["..."]*4);
		
		# Add row with summary
		footer[2] = total;
		rows.append("");
		rows.append(footer);
		
		return (headers,rows);
	
	def balance(self):
		
		headers = ["User", "Total"];
		footer  = ["Total", None];
		rows    = list();
		total   = 0;
		
		# Get all users
		users = self.repos.users.get_all();
		
		# Generate row for each user
		for user in users:
			history = self.services.statement.history(user, 1);
			amount  = history[1][-1][2];
			total  += amount;
			rows.append([user.nick, amount]);
		
		# Generate table footer
		footer[1] = total;
		rows.append("");
		rows.append(footer);
		
		return (headers,rows);

