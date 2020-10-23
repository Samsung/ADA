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

class Correct(Base):
	
	name   = 'correct';
	help   = 'Create correction for current delivery.';
	role   = ada.entities.Role.REGULAR;
	stages = ada.entities.Stage.ADJUST;
	
	def init(self):
		
		self.add_argument("user",
			type = self.argtypes.user,
			help = "Mention of the user related to the correction.");
		
		self.add_argument("price",
			type = self.argtypes.money,
			help = "Amount of the correction, it has to be in the money or"\
			       " simple calculation format, examples: 1, 2.50, 4+2-0.50.");
		
		self.add_argument("note",
			nargs = "+",
			help  = "Note with the description of the correction.");
	
	def exec(self, whoami, author, channel, content, argv, args, log, user, delivery):
		
		# Create useful aliases
		corrector = user;
		purchaser = args.user;
		price     = args.price;
		note      = " ".join(args.note);
		
		# Create new correction for the current delivery
		correction = self.services.adjustment.correct(corrector, purchaser, price, note, log);
		
		# Return command summary message
		msg = "New correction was created, its amount is {}.";
		msg = msg.format(self.argtypes.money.format(correction.price));
		return msg;

