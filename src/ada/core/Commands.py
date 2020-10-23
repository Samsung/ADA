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

import ada;

class Commands:
	
	def __new__(cls,
			base,
			arguments,
			database,
			services,
			argtypes):
		
		# Placeholder objects, for all commands
		placeholder = dict();
		
		# Get list with all subclasses of command base class
		subclasses = base.__subclasses__();
		
		# For each command class, create a new object
		objects = [subclass(arguments, database, services, argtypes, placeholder) for subclass in subclasses];
		
		# Create a dictionary, which contains objects for all commands
		commands = {command.name: command for command in objects};
		
		# Update placeholder with commands objects
		placeholder.update(commands);
		
		# Return dictionary of commands
		return commands;

