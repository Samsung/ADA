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

import time;

class Sleep(Base):
	
	name = 'sleep';
	help = 'Got to sleep for few seconds.';
	exce = "Error while sleeping";
	role = ada.entities.Role.ADMIN;
	
	def init(self):
		
		self.add_argument("seconds",
			type = float,
			help = "How long service should sleep in number of seconds.");
	
	def exec(self, whoami, author, channel, content, argv, args, log, user, delivery):
		
		# Create useful aliases
		seconds = args.seconds;
		
		# Number of seconds has to be positive number
		if seconds < 0.0:
			msg = 'Number of seconds has to be positive!';
			raise ValueError(msg);
		
		# Sleep for few seconds
		time.sleep(seconds);
		
		# Return command summary message
		msg = 'ADA slept for {} seconds.';
		msg = msg.format(seconds);
		return msg;

