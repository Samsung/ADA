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
	
	def call(self,
			value : str)\
			-> ada.entities.Role:
		
		value = value.upper();
		
		# Make sure, that role exists
		if not value in ada.entities.Role.__members__:
			msg = "Role {} does not exists!";
			msg = msg.format(value);
			raise KeyError(msg);
		
		# Convert role text to enum
		role = ada.entities.Role[value];
		
		return role;

