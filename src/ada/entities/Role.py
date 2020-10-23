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

import enum;

class Role(enum.IntEnum):
	"""
		List of roles for managing application users permissions.
		Documentation for roles is in docs/roles.md file.
		This entity does not have representation in database!
	"""
	
	DELETED    = -30; # The account deleted, saldo is already settled
	SETTLEMENT = -20; # The account is pending for the balance settlement
	BANNED     = -10; # The account with temporary ban for all commands
	NONE       =   0; # This user does not register his account yet
	UNACCEPTED =  10; # The account is pending for acceptance
	REGULAR    =  20; # The account with regular privileges
	MODERATOR  =  30; # The account with moderator privileges
	ADMIN      =  40; # The account with administrator privileges
	ROOT       =  50; # The account with root privileges

