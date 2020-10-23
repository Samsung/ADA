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

class Balance(Base):
	
	name = "balance";
	help = "Print all accounts balance.";
	role = ada.entities.Role.REGULAR;
	
	def exec(self, whoami, author, channel, content, argv, args, log, user, delivery):
		
		# Generate balance for all users accounts
		headers,rows = self.services.statement.balance();
		
		# Format data in column that contain total money
		rows = [[row[0], self.argtypes.money.format(row[1])] for row in rows if row];
		
		# Return command summary message
		table = tabulate.tabulate(rows, headers, tablefmt="simple", colalign=("left","right"), disable_numparse=True);
		table = "```\n{}\n```".format(table);
		return table;

