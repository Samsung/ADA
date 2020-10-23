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

class User(Base):
	
	def call(self,
			value : str)\
			-> ada.entities.User:
		
		regex = r"^<@!?([0-9]+)>$";
		match = re.search(regex, value);
		
		if not match:
			msg = "Invalid user mention string: {}!";
			msg = msg.format(value);
			raise ArgumentTypeError(msg);
		
		number = match.group(1);
		
		try:
			did = int(number);
		except ValueError:
			msg = "Invalid user discord id number: {}!";
			msg = msg.format(number);
			raise ArgumentTypeError(msg);
		
		user = self.repos.users.get_one(did=did);
		
		if not user:
			msg = "User with discord id {} does not exists!";
			msg = msg.format(did);
			raise ArgumentTypeError(msg);
		
		return user;

