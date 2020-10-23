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

class Finish(Base):
	
	name   = "finish";
	help   = "Finish current delivery.";
	exce   = "Error while finishing delivery";
	role   = ada.entities.Role.MODERATOR;
	stages = ada.entities.Stage.ADJUST;
	epilog = """
		Finishing current delivery is allowed only then,
		when sum of all ordered items, payment
		and corrections are summing into zero.
	""";
	
	def exec(self, whoami, author, channel, content, argv, args, log, user, delivery):
		
		# Finish current delivery
		delivery = self.services.delivery.finish(log);
		
		# Return command summary message
		msg = "Delivery {} finished.";
		msg = msg.format(delivery.id);
		return msg;

