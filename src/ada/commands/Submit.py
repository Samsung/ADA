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

class Submit(Base):
	
	name   = "submit";
	help   = "Submit restaurant voting candidate for current delivery.";
	role   = ada.entities.Role.REGULAR;
	stages = ada.entities.Stage.GATHER;
	
	def init(self):
		
		self.add_argument("restaurants",
			nargs = "+",
			type  = self.argtypes.restaurant,
			help  = "List of restaurants keys, that will be submitted to voting.");
	
	def exec(self, whoami, author, channel, content, argv, args, log, user, delivery):
		
		# Create useful aliases
		gathering   = delivery.re_gathering;
		restaurants = args.restaurants;
		
		# Submit voting candidate
		candidates = self.services.gathering.submits(gathering, restaurants, log);
		
		# Generate candidates message string
		candidates_str = [c.re_restaurant.name for c in candidates];
		candidates_str = ", ".join(candidates_str);
		
		# Return command summary message
		msg = "Submitted candidates: {}.";
		msg = msg.format(candidates_str);
		return msg;

