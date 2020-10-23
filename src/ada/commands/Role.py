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

class Role(Base):
	
	name   = "role";
	help   = "Change privileges, accept, ban and delete users accounts.";
	exce   = "Error while changing account role";
	role   =  ada.entities.Role.ADMIN;
	epilog = """
		DELETED    - The account deleted, saldo is already settled.
		SETTLEMENT - The account is pending for the balance settlement.
		BANNED     - The account with temporary ban for all commands.
		NONE       - This user does not register his account yet.
		UNACCEPTED - The account is pending for acceptance.
		REGULAR    - The account with regular privileges.
		MODERATOR  - The account with moderator privileges.
		ADMIN      - The account with administrator privileges.
		ROOT       - The account with root privileges.
	""";
	
	def init(self):
		
		self.add_argument("user",
			type = self.argtypes.user,
			help = "Mention of the user, which role will be changed.");
		
		self.add_argument("role",
			type = self.argtypes.role,
			help = "User account new role, see help for more details.");
	
	def exec(self, whoami, author, channel, content, argv, args, log, user, delivery):
		
		# Create useful aliases
		user = args.user;
		role = args.role;
		
		# Place order for current delivery
		user = self.services.user.change_role(user, role, log);
		
		# Return command summary message
		msg = "Role for user {} was changed to {}.";
		msg = msg.format(user.mention, user.role);
		return msg;

