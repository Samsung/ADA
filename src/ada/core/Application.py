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

class Application:
	"""
			This function is a project entrypoint, its create every object required
			by discord client and execute client event loop. This is a good place,
			to start project analyzation.
	"""
	
	def __init__(self, argv : typing.List[str] = None) -> int:
		"""
		"""
		
		# Parse application command line arguments
		self.arguments = ada.core.Arguments(
			argv = argv,
		);
		
		# Create and initialize logger object
		self.logger = ada.core.Logger(
			verbosity = self.arguments.verbosity,
			logfile   = self.arguments.logfile,
		);
		
		# Initialize object-relational mapping
		self.database = ada.core.Database(
			base_ents  = ada.entities.Base,
			base_repos = ada.repositories.Base,
			file       = self.arguments.database,
			echo       = self.arguments.queries
		);
		
		# Create objects for each service
		self.services = ada.core.Services(
			base      = ada.services.Base,
			arguments = self.arguments,
			database  = self.database,
		);
		
		# Create command arguments parsers
		self.argtypes = ada.core.Argtypes(
			base      = ada.argtypes.Base,
			arguments = self.arguments,
			database  = self.database,
			services  = self.services,
		);
		
		# Create object for each command
		self.commands = ada.core.Commands(
			base      = ada.commands.Base,
			arguments = self.arguments,
			database  = self.database,
			services  = self.services,
			argtypes  = self.argtypes,
		);
		
		# Create handler objects for client events
		self.handlers = ada.core.Handlers(
			base      = ada.handlers.Base,
			app       = self,
			arguments = self.arguments,
			logger    = self.logger,
			database  = self.database,
			services  = self.services,
			argtypes  = self.argtypes,
			commands  = self.commands,
		);
		
		# Create discord client object
		self.client = ada.core.Client(
			handler_ready    = self.handlers.ready,
			handler_periodic = self.handlers.periodic,
			handler_finish   = self.handlers.finish,
			handler_message  = self.handlers.message,
			handler_format   = self.handlers.formatter,
			conf_channel     = self.arguments.channel,
			conf_delay       = self.arguments.delay,
			conf_loopback    = False,
			logger           = self.logger,
		);
	
	def run(self):
		"""
			This function is connection application to the discord and start
			main event loop.
		"""
		
		# Run client and save exit code
		code = self.client.run(self.arguments.token);
		
		# Return exit code
		return code;

