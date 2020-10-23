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

class Start(Base):
	
	name   = 'start';
	help   = 'Start new delivery process.';
	exce   = 'Error while starting delivery';
	role   =  ada.entities.Role.MODERATOR;
	stages = [ada.entities.Stage.SLEEP];
	epilog = "Skipping voting process is allowed only for admins.";
	
	def init(self):
		
		self.add_argument("restaurant",
			nargs = "?",
			type  = self.argtypes.restaurant,
			help  = "If you want to skip the voting process, then enter here restaurant key.");
	
	def exec(self, whoami, author, channel, content, argv, args, log, user, delivery):
		
		# Create useful aliases
		restaurant = args.restaurant;
		
		# Higher role is required, to skip voting process
		if restaurant and user.role < ada.entities.Role.ADMIN:
			msg = "Administrator role is required, to skip voting process.";
			raise Exception(msg);
		
		# Starting new delivery
		delivery = self.services.delivery.start(log, restaurant);
		
		# Return success summary message
		msg = "New delivery started.";
		return msg;

