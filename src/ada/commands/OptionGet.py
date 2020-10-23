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

class OptionGet(Base):
	
	name    = 'opt-get';
	info    = 'Get values from options variables.';
	role = ada.entities.Role.NONE;
	argsMin = 0;
	argsMax = 1;
	help    = """
		This command will print values if configuration options.
		If option name is not given, then all options will be printed.
		
		Command arguments:
		* name  - Identification key of the option to print.
	""";
	
	def exec(self, prefix, author, channel, content, log, user, delivery, args):
		
		msg = "NotImplementedError";
		raise NotImplementedError(msg);
		
		self.services.option
		
		if len(args) < 2:
			val = ada.core.Config.get(key);
			msg = 'Value of key {} is: {}';
			msg = msg.format(key, val);
			return msg;
		
		# Create variables for table generating
		header = ['Key', 'Value', 'Description'];
		rows   = ada.core.Config.all();
		
		# Generate ascii table with results
		table = str(tabulate.tabulate(rows, header, tablefmt="simple"));
		table = "```\n{}\n```".format(table);
		
		# Return help
		return table;

