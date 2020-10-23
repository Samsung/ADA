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

class Accept(Base):
	
	name = "accept";
	help = "Accept user account.";
	exce = "Error while accepting new user account";
	role = ada.entities.Role.MODERATOR;
	
	def init(self):
		
		self.add_argument("user",
			type = self.argtypes.user,
			help = "Mention of the new user, which account will be accepted.");
	
	def exec(self, whoami, author, channel, content, argv, args, log, user, delivery):
		
		# Create useful aliases
		new_user = args.user;
		
		# Set new nick for user
		self.services.user.accept(new_user, log);
		
		# Return command summary message
		msg = "New user {} account accepted.";
		msg = msg.format(new_user.mention);
		return msg;

