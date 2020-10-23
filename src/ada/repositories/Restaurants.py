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

class Restaurants(Base):
	"""
		Basic repository class for Restaurant entity.
	"""
	
	def init(self):
		self.entity = ada.entities.Restaurant;
	
	def argparse(self,
			value):
		
		restaurant = self.get_one(**filters);
		
		if not restaurant:
			msg = 'Restaurant {} does not exists.';
			msg = msg.format(name);
			raise Exception(msg);
		
		return restaurant;

