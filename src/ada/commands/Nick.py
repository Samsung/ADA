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

class Nick(Base):
	
	name = 'nick';
	help = 'Change your nickname.';
	exce = 'Error while changing nickname';
	role = ada.entities.Role.REGULAR;
	
	def init(self):
		
		self.add_argument("nick",
			help = "New nick.");
	
	def exec(self, whoami, author, channel, content, argv, args, log, user, delivery):
		
		# Create useful aliases
		nick = args.nick;
		
		# Set new nick for user
		self.services.user.set_nick(user, nick);
		
		# Return command summary message
		msg = "User {} has now new nick {}.";
		msg = msg.format(user.mention, user.nick);
		return msg;

