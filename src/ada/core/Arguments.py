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
import argparse;
import logging;
import pathlib;
import typing;
import yaml;

class Arguments(argparse.Namespace):
	"""
		Class for parsing application command line arguments.
	"""
	
	def __new__(cls, argv : typing.List[str] = None) -> argparse.Namespace:
		"""
			Initialize application, parse arguments, load configuration,
			create logger and return object with configuration.
		"""
		
		# Create parser for command line arguments
		parser = cls.create_parser();
		
		# First parse of command line arguments
		raw_args = parser.parse_args(argv);
		
		# Load configuration file with new defaults
		defaults = cls.load_defaults(raw_args.config);
		
		# Update parser with new defaults
		cls.update_defaults(parser, defaults);
		
		# Parse again command line arguments
		args = parser.parse_args(argv);
		
		# Post processing for arguments object
		cls.post_parsing(args, parser, raw_args, defaults);
		
		# Return object with arguments
		return args;
	
	def create_parser() -> argparse.ArgumentParser:
		"""
			Create and configure object of parser for command line arguments.
		"""
		
		# Prepare and format texts for a parser
		version = "{} {}".format(ada.__title__, ada.__version__);
		epilog  = "Authors: %s" % ada.__author__;
		
		# Create new object of parser
		parser = argparse.ArgumentParser(
			prog        = ada.__name__,
			description = ada.__short__,
			epilog      = epilog,
			add_help    = False,
		);
		
		parser.add_argument("-c", "--config",
		                    metavar = "PATH",
		                    type    = pathlib.Path,
		                    help    = "Path to yaml file, which contains"\
		                    " configuration with default values of command"\
		                    " line arguments.");
		
		parser.add_argument("-t", "--token",
		                    metavar = "TOKEN",
		                    type    = str,
		                    help    = "Access token for Discord bot.");
		
		parser.add_argument("-e", "--env",
		                    metavar = "NAME",
		                    default = "dev",
		                    type    = str,
		                    help    = "Environment name, typically it is one"\
		                    " of: prod, test, dev.");
		
		parser.add_argument("-d", "--database",
		                    metavar = "PATH",
		                    type    = pathlib.Path,
		                    help    = "Path to database file, if empty, then"\
		                    " temporary database will be created.");
		
		parser.add_argument("-C", "--channel",
		                    metavar = "NAME",
		                    default = "ada_delivery",
		                    type    = str,
		                    help    = "Name of Discord channel to listen on.");
		
		parser.add_argument("-D", "--delay",
		                    metavar = "SECONDS",
		                    default = 0.1,
		                    type    = float,
		                    help    = "Minimal delay in between periodic events.");
		
		parser.add_argument("-L", "--limit",
		                    metavar = "CHARS",
		                    default = 1600,
		                    type    = int,
		                    help    = "Limit of characters in a single discord message.");
		
		parser.add_argument("-m", "--manners",
		                    action = "store_true",
		                    help   = "Send a hello and goodbye message.");
		
		parser.add_argument("-l", "--logfile",
		                    metavar = "PATH",
		                    type    = pathlib.Path,
		                    help    = "Path to file where log information"\
		                    " will be saved.");
		
		parser.add_argument("-Q", "--queries",
		                    action = "store_true",
		                    help   = "If this flag is set, then database"\
		                    " queries will be printed.");
		
		parser.add_argument("-v", "--verbosity",
		                    metavar = "LEVEL",
		                    default = "WARNING",
		                    type    = str,
		                    choices = logging._nameToLevel.keys(),
		                    help    = "Verbosity level name for logging module"\
		                    " ({}).".format(", ".join(logging._nameToLevel.keys())));
		
		parser.add_argument("-V", "--version",
		                    action  = "version",
		                    version = version,
		                    help    = "Show version information and exit.");
		
		parser.add_argument("-h", "--help",
		                    action = "help",
		                    help   = "Show help message and exit.");
		
		return parser;
	
	def load_defaults(path : pathlib.Path) -> typing.Dict:
		"""
			Load configuration dictionary from yaml file.
			
			Args:
				path: Path to yaml file with configuration.
		"""
		
		# Stop, if configuration file is not given
		if not path:
			return None;
		
		# Make sure, that configuration file exists
		if not path.is_file():
			msg = "Configuration file does not exists ({})!";
			raise FileNotFoundError(msg.format(path));
		
		# Load and parse configuration file
		with open(path, "r") as stream:
			config = yaml.load(stream);
		
		# Make sure, that configuration is a dictionary
		if not isinstance(config, dict):
			msg = "Configuration object has to be a dictionary!";
			raise TypeError(msg);
		
		# Return configuration dictionary
		return config;
	
	def update_defaults(
			parser   : argparse.ArgumentParser,
			defaults : typing.Dict) -> argparse.Namespace:
		"""
			Update actions in existing parser object, set new defaults
			based on dictionary loaded from configuration file.
		"""
		
		# Do nothing if there is not defaults
		if not defaults:
			return;
		
		# Create dictionary with all supported parsing actions
		actions = {action.dest: action for action in parser._get_optional_actions()
		           if action.dest not in ["help", "version", "config"]};
		
		# For each default value from dictionary
		for key,default in defaults.items():
			
			# Raise exception if action does not exists
			if not key in actions:
				msg = "Option {} does not exists!";
				raise KeyError(msg.format(key));
			
			# Make sure, that default value has correct type
			# TODO: Options with parameter action=store_true,
			# does not have type, how to check them?
			if actions[key].type:
				default = actions[key].type(default);
			
			# Set new default value in parser
			parser.set_defaults(**{key:default});
	
	def post_parsing(args, parser, raw_args, defaults):
		"""
		"""
		
		# Add local variables to arguments object
		args._parser   = parser;
		args._raw_args = raw_args;
		args._defaults = defaults;
		
		# Check if discord token is given
		if not args.token:
			msg = "Token for Discord bot is required!";
			raise ValueError(msg);

