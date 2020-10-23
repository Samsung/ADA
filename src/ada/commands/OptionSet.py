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

class OptionSet(Base):
	
	name    = 'opt-set';
	info    = 'Set values into options variables.';
	role = ada.entities.Role.NONE;
	argsMin = 2;
	argsMax = 2;
	help    = """
		Command arguments:
		* name  - Identification key of the option to be set.
		* value - Value that will be set into option.
	""";
	
	def exec(self, prefix, author, channel, content, log, user, delivery, args):
		
		msg = "NotImplementedError";
		raise NotImplementedError(msg);
		
		# Rename command parameters
		name  = args[0];
		value = args[1];
		
		# Set new value into option
		self.services.option.set(name, value);
		
		
		val = ' '.join(args[1:]);
		
		ada.core.Config.set(key, val);
		
		msg = 'New value of key {} is: {}';
		msg = msg.format(key, val);
		return msg;

