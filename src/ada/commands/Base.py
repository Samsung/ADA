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
import typing
import argparse;
import tabulate;

class Base():
	"""
		Base class for all bot commands.
	"""
	
	# Name of command, it is required.
	name = None;
	
	# A single line sentence to describe a behavior of the command,
	# it is required.
	help = None;
	
	# Prefix that will be added to the error message, if command raise
	# some exception. It is not required, but is highly recommended.
	exce = None;
	
	# Minimal role required to access to this command, it is required.
	role = None;
	
	# Array of stages in which command is allowed, if this attribute
	# has value None then command is allowed in every stage.
	stages = None;
	
	# Additional informations about command behavior, that is displayed
	# in the command help details.
	epilog = None;
	
	# Custom class for parsing arguments, to redefine default behavior
	# from exit, to raise exception, when parsing error occurred .
	class ArgumentParserThrower(argparse.ArgumentParser):
		def error(self, message):
			if message.startswith("argument key: "):
				message = message[14:];
			raise ValueError(message);
	
	def init(self)\
			-> None:
		"""
			Custom initialization of command object, it is right place
			to add arguments definition into command arguments parser.
		"""
		
		pass;
	
	def exec(self,
			whoami   : int,
			author   : int,
			channel  : str,
			content  : str,
			argv     : typing.List[str],
			args     : argparse.Namespace,
			log      : ada.entities.Log,
			user     : ada.entities.User,
			delivery : ada.entities.Delivery)\
			-> str:
		"""
			Method that execute command code and return response,
			it has to be implemented for command correct working.
		"""
		
		msg = "This command is not implemented!";
		raise NotImplementedError(msg);
	
	def add_argument(self,
			*args,
			**kwargs)\
			-> None:
		"""
			Function for simple adding a parsing arguments definition
			into command arguments parser.
		"""
		
		self.parser.add_argument(*args, **kwargs);
	
	def __init__(self,
			arguments,
			database,
			services,
			argtypes,
			commands):
		"""
		"""
		
		parser = Base.ArgumentParserThrower(
			prog        = self.name,
			description = self.help,
			epilog      = self.epilog,
			add_help    = False,
		);
		
		self.arguments = arguments;
		self.database  = database;
		self.repos     = database.repos;
		self.services  = services;
		self.argtypes  = argtypes;
		self.commands  = commands;
		self.parser    = parser;
		
		if self.stages and not isinstance(self.stages, list):
			self.stages = [self.stages];
		
		self.init();

