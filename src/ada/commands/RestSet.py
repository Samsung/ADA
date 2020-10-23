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

class RestSet(Base):
	
	name = 'rest-set';
	help = "Change information in restaurant list.";
	exce = "Error while changing a restaurant";
	role = ada.entities.Role.ADMIN;
	
	def init(self):
		
		self.add_argument("key",
			type = self.argtypes.restaurant,
			help = "Short name of the restaurant.");
		
		self.add_argument("field",
			choices = ["key", "name", "url", "active"],
			help    = "Name of the field to be changed.");
		
		self.add_argument("value",
			help  = "Value to be settled into field.");
	
	def exec(self, whoami, author, channel, content, argv, args, log, user, delivery):
		
		# Create useful aliases
		restaurant = args.key;
		field      = args.field;
		value      = args.value;
		
		# Convert value to boolean if required
		if field == "active":
			if value == "1":
				value = True;
			elif value == "0":
				value = False;
			else:
				msg = "Value of the active field has to be 0 or 1.";
				raise ValueError(msg);
		
		# Add new restaurant into database
		restaurant = self.services.restaurant.update(restaurant, field, value, log);
		
		# Return success summary message
		msg = "Restaurant {} successfully changed.";
		msg = msg.format(restaurant.key);
		return msg;

