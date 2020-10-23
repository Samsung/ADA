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

class RestAdd(Base):
	
	name = "rest-add";
	help = "Add new restaurant to restaurant list.";
	exce = "Error while adding a restaurant";
	role = ada.entities.Role.MODERATOR;
	
	def init(self):
		
		self.add_argument("key",
			help = "Short name of the restaurant.");
		
		self.add_argument("name",
			nargs = "?",
			help  = "Full name of the restaurant.");
		
		self.add_argument("url",
			nargs = "?",
			help  = "Url to the restaurant.");
	
	def exec(self, whoami, author, channel, content, argv, args, log, user, delivery):
		
		# Create useful aliases
		key  = args.key;
		name = args.name;
		url  = args.url;
		
		# If name does not exists, then it is equal to key
		if not name:
			name = key;
		
		# Force proper format for empty url
		if not url:
			url = None;
		
		# Add new restaurant into database
		restaurant = self.services.restaurant.create(key, name, url, log);
		
		# Return success summary message
		msg = "Restaurant {} successfully created.";
		msg = msg.format(restaurant.key);
		return msg;

