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

class Etofa(Base):
	
	name   = 'etofa';
	help   = 'Set estimated time of arrival for current delivery.';
	role   = ada.entities.Role.REGULAR;
	stages = ada.entities.Stage.SUMMARY;
	
	def init(self):
		
		self.add_argument("time",
			type = self.argtypes.time,
			help = "Estimated time of arrival in HH:MM format.");
	
	def exec(self, whoami, author, channel, content, argv, args, log, user, delivery):
		
		# Create useful aliases
		time = args.time;
		
		# Change ETofA for the current delivery
		payment = self.services.summary.etofa(time);
		
		# Return command summary message
		msg = 'Current ETofA is changed to {}.';
		msg = msg.format(payment.etofa);
		return msg;

