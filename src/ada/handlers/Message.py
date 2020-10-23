#!/usr/bin/env python3#!/usr/bin/env python3
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

import ada;
import logging;
import shlex;
import traceback;

class Message(Base):
	"""
		Implementation of message event handler for discord client.
	"""
	
	def __init__(self, *args, **kwargs):
		
		super().__init__(*args, **kwargs);
		
		self.commands = self.commands;
		self.channel  = self.arguments.channel;
	
	def __call__(self,
			whoami  : int,
			author  : int,
			channel : str,
			content : str):
		"""
			
		"""
		
		try:
			# Receive and process a request
			response = self.command(whoami, author, channel, content);
		except Exception as e:
			logging.debug(traceback.format_exc());
			response = '[EXC] {}'.format(e);
			# Logging for command exception
			logging.debug("Command exce: %s", e);
		
		# Return if response is empty
		if not response:
			return;
		
		# Logging for command response
		logging.debug("Command response: %s", response);
		
		# Add sender mention and send back
		return '<@{}>: {}'.format(author, response);
	
	def command(self,
			whoami  : int,
			author  : int,
			channel : str,
			content : str):
		
		# Prepare expected bot prefix in form of a mention 
		mention = ada.entities.User(did=whoami).mention;
		
		# Check if message content exists
		if not content:
			return;
		
		# Check if message is received from right channel
		if channel != self.channel and channel is not None:
			return;
		
		# Check if message starts with right prefix
		if channel and not content.replace("!", "").startswith(mention):
			return;
		
		# Create and get basic data from database
		delivery = self.database.repos.deliveries.get_current();
		log      = self.database.repos.logs.create_from_message(author, whoami, channel, content, 1, delivery);
		user     = self.database.repos.users.get_one(did=author);
		
		# If user exists, then update his action
		if user:
			user.re_log_action = log;
			self.database.session.commit();
		
		# Split message content into arguments
		argv = shlex.split(str(content));
		
		# If bot mention argument exists, then remove it
		argv = argv[1:] if channel else argv;
		
		# Checks for prefix and command name
		if len(argv) < 1:
			raise Exception('Command name missing!');
		if argv[0] not in self.commands:
			raise Exception('Command name not found!');
		
		# Get object of current command
		command = self.commands[argv[0]];
		
		# Test if current user permissions are enough for this command
		if not user and command.role > ada.entities.Role.NONE:
			msg  = 'Access denied: account is required!\n';
			msg += 'Register your account with command: register';
			raise Exception(msg);
		elif user and command.role > user.role:
			msg = 'Access denied: at least {} role is required!';
			msg = msg.format(command.role.name);
			raise Exception(msg);
		
		# Test if current delivery stage is appropriate for this command
		stage = self.database.repos.deliveries.get_stage();
		if command.stages and stage not in command.stages:
			msg = 'Command {} is not permitted in stage {}.';
			msg = msg.format(command.name, stage);
			raise Exception(msg);
		
		# Parse command arguments using ArgumentParser object
		args = command.parser.parse_args(argv[1:]);
		
		# Logging for command variables
		logging.debug("Command vars: %s, %s, %s, %s, %s", command.name, log, user, delivery, args);
		
		try:
			# Try to execute command and commit changes
			response = command.exec(whoami, author, channel, content, argv, args, log, user, delivery);
			self.database.session.commit();
			return response;
		except Exception as e:
			# In the case of an exception, rollback changes and return exception message
			self.database.session.rollback();
			
			# TODO
			raise e;
			
			if not command.exce:
				raise e;
			raise Exception(command.exce.format(e)) from e;

