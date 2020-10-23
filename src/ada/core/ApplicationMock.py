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
import typing;
from .Application import Application;

class ApplicationMock(Application):
	
	def __init__(self,
			argv : typing.List[str] = None)\
			-> int:
		"""
		"""
		
		super().__init__(argv);
	
	def run(self):
		"""
		"""
		
		msg = "This is only application mock, run cannot be called!";
		raise NotImplementedError(msg);
	
	def message(self, *args):
		"""
			This function exists only for test purpose! It is simulating
			a connection with discords and different events.
			Especially a message event.
		"""
		
		whoami  = 99;
		author  =  1;
		channel = self.arguments.channel;
		content = "";
		
		if len(args) == 1:
			content = args[0];
		elif len(args) == 2:
			author  = args[0];
			content = args[1];
		elif len(args) == 3:
			author  = args[1];
			channel = args[0];
			content = args[2];
		elif len(args) == 4:
			whoami  = args[1];
			author  = args[2];
			channel = args[0];
			content = args[3];
		else:
			msg = 'Too many arguments.';
			raise Exception(msg);
		
		whoami = int(whoami);
		author = int(author);
		
		content = f"<@{whoami}> {content}";
		
		result = self.handlers.message.command(whoami, author, channel, content);
		
		return result;

