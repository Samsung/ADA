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

class RestList(Base):
	
	name = 'rest-list';
	help = 'Show the list of restaurants.';
	exce = "Error while listing restaurants";
	role = ada.entities.Role.REGULAR;
	
	def init(self):
		
		self.add_argument("-i", "--inactive",
			action = "store_true",
			help   = "Show also restaurants that are inactive.");
	
	def exec(self, whoami, author, channel, content, argv, args, log, user, delivery):
		
		# Create useful aliases
		inactive  = args.inactive;
		
		# Generate restaurants table header and rows
		header,rows = self.services.restaurant.listing(inactive);
		
		# Generate ascii table with results
		table = str(tabulate.tabulate(rows, header, tablefmt="simple"));
		table = "\n```\n{}\n```".format(table);
		
		# Return restaurants table
		return table;

