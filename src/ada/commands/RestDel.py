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

class RestDel(Base):
	
	name = "rest-del";
	help = "Delete restaurant from restaurant list.";
	exce = "Error while deleting a restaurant";
	role = ada.entities.Role.ADMIN;
	
	def init(self):
		
		self.add_argument("key",
			type = self.argtypes.restaurant,
			help = "Short name of the restaurant.");
	
	def exec(self, whoami, author, channel, content, argv, args, log, user, delivery):
		
		# Create useful aliases
		restaurant = args.key;
		
		# Remove restaurant from database
		restaurant = self.services.restaurant.delete(restaurant, log);
		
		# Return success summary message
		msg = "Restaurant {} successfully deleted.";
		msg = msg.format(restaurant.key);
		return msg;

