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
import logging;
import pathlib;

class Logger(logging.Logger):
	"""
	"""
	
	def __new__(cls,
			verbosity : str          = None,
			logfile   : pathlib.Path = None):
		"""
		"""
		
		# Get code of the current verbosity
		try:
			level = logging._nameToLevel[verbosity];
		except:
			msg = "Incorrect verbosity level name ({})!";
			raise ValueError(msg.format(verbosity));
		
		# Create and configure logger for this module
		logger = logging.getLogger(ada.__name__);
		logger.setLevel(level);
		
		# Create and add default logger handler
		format    = "%(process)s %(thread)s: %(message)s"
		formatter = logging.Formatter(format);
		handler   = logging.StreamHandler();
		handler.setFormatter(formatter);
		logger.addHandler(handler);
		
		# Set required logger level, to all existing loggers
#		for key,logger in logging.Logger.manager.loggerDict.items():
#			with contextlib.suppress(AttributeError):
#				logger.setLevel(level);
		
		# Print current verbosity mode
		msg = "Current verbosity mode: %s";
		logger.warning(msg, verbosity);
		
		return logger;

