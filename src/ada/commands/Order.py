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
	
	name   = "order";
	help   = "Create or update order item for current delivery.";
	exce   = "Error while creating/updating order item";
	role   = ada.entities.Role.REGULAR;
	stages = ada.entities.Stage.ORDER;
	
	def init(self):
		
		self.add_argument("price",
			type = self.argtypes.money,
			help = "Price of the order item, it has to be in the money or"\
			       " simple calculation format, examples: 1, 2.50, 4+2-0.50.");
		
		self.add_argument("note",
			nargs = "+",
			help  = "Note with the description of the order item.");
	
	def exec(self, whoami, author, channel, content, argv, args, log, user, delivery):
		
		# Create useful aliases
		note  = " ".join(args.note);
		price = args.price;
		
		# Place order for current delivery
		item = self.services.order.create_or_update_item(user, price, note, log);
		
		# Return command summary message
		msg = "New order item was created, its price is {}.";
		msg = msg.format(self.argtypes.money.format(item.price));
		return msg;

