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

class Help(Base):
	
	name = "help";
	help = "Show help information about commands.";
	role = ada.entities.Role.NONE;
	
	def init(self):
		
		self.add_argument("command",
			nargs = "?",
			help  = "Command name for detailed informations.");
	
	def exec(self, whoami, author, channel, content, argv, args, log, user, delivery):
		
		# Create useful aliases
		command = args.command;
		
		# Get help for one or all commands
		if command:
			msg = self.one(command);
		else:
			msg = self.all();
		
		# Return help message
		return msg;
	
	def one(self, name):
		
		# Check if command exists
		if not name in self.commands:
			msg = "Command name not found!";
			raise KeyError(msg);
		
		# Save command objects
		command = self.commands[name];
		
		# Get command role name
		role = command.role.name;
		
		# Generate command stages list
		if command.stages:
			stages = [stage.name for stage in command.stages];
			stages = ", ".join(stages);
		else:
			stages = "";
		
		# Generate command help
		usage = command.parser.format_help();
		usage = usage[7+len(name):];
		
		# Generate response with command help
		response  =  "\n```\n";
		response += f"Name: {name}\n";
		response += f"Role: {role}\n";
		response += f"Stages: {stages}\n";
		response += f"Args:{usage}\n";
		response += "```\n";
		
		# Return help
		return response;
	
	def all(self):
		
		# Define table headers
		headers = ["Name", "Role", "Help"];
		
		# Get list of all commands objects
		commands = [command for name,command in self.commands.items()];
		
		# Generate rows with commands informations
		rows = [[cmd.name, cmd.role.name, cmd.help] for cmd in commands];
		
		# Sort by commands names
		rows = sorted(rows, key=lambda r: r[0]);
		
		# Generate ascii table with commands
		table = str(tabulate.tabulate(rows, headers, tablefmt="simple"));
		
		# Find commands specific for this stage
		stage    = self.database.repos.deliveries.get_current();
		specific = [c.name for c in commands if c.stages and stage in c.stages];
		specific = " ".join(specific);
		
		# Generate response with commands list
		response  = "\n```\n";
		response += "Ada (Automatic Delivery Aid) - discord bot for ordering food\n";
		response += "\n";
		response += "For more details type command: help COMMAND_NAME\n";
		response += "\n";
		response += "Commands specific for this stage: {}\n".format(specific);
		response += "\n";
		response += "Table of commands:\n";
		response += table + "\n";
		response += "```\n";
		
		# Return help
		return response;

