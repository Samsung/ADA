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

class History(Base):
	
	name = "history";
	help = "Print history of your balance.";
	role = ada.entities.Role.REGULAR;
	
	def init(self):
		
		self.add_argument("limit",
			nargs   = "?",
			metavar = "limit",
			type    = int,
			default = 10,
			choices = range(1, 101),
			help    = "How many balance records should be displayed.");
	
	def exec(self, whoami, author, channel, content, argv, args, log, user, delivery):
		
		# Create useful aliases
		limit = args.limit;
		
		# Generate users table header and rows
		headers,rows = self.services.statement.history(user, limit);
		
		# Format operation money amounts
		for row in rows:
			if not row:
				continue;
			if row[0] == "...":
				continue;
			if row[0]:
				row[0] = row[0].strftime("%Y-%m-%d %H:%M:%S");
			if row[2]:
				row[2] = self.argtypes.money.format(row[2]);
		
		# Return command summary message
		table = tabulate.tabulate(rows, headers, tablefmt="simple");
		table = "```\n{}\n```".format(table);
		return table;

