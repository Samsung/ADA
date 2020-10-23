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

class Register(Base):
	
	name   = "register";
	help   = "Create a new user account.";
	exce   = "Error during user registration";
	role   = ada.entities.Role.NONE;
	epilog = """
		Creating a new user account in ADA database, which will be bound with
		your discord user. New accounts may require an activation by one of
		the administrators.
	""";
	
	def init(self):
		
		self.add_argument("nick",
			help = "Human readable name of your account (format: ^[a-zA-Z0-9_.-]{3,}$).");
	
	def exec(self, whoami, author, channel, content, argv, args, log, user, delivery):
		
		# Create useful aliases
		did  = author;
		nick = args.nick;
		
		# Create account for the new user
		user = self.services.user.register(did, nick, log);
		
		# Return command summary message
		msg = "User {} successfully registered with role {}.";
		msg = msg.format(user.nick, user.role);
		return msg;

