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

class Next(Base):
	
	name   = "next";
	help   = "Go to next delivery stage.";
	exce   = "Error while moving to next delivery stage";
	role   = ada.entities.Role.MODERATOR;
	stages = [
		ada.entities.Stage.GATHER,
		ada.entities.Stage.VOTE,
		ada.entities.Stage.ORDER,
		ada.entities.Stage.SUMMARY,
	];
	
	def exec(self, whoami, author, channel, content, argv, args, log, user, delivery):
		
		# Save old delivery stage
		stage_old = delivery.stage;
		
		# Get service related to old delivery stage
		service = self.services.management.get_service(self.services, stage_old);
		
		# Go to the next delivery stage
		result = service.next();
		result = f"\n{result}" if result else "";
		
		# Get new delivery stage
		stage_new = delivery.stage;
		
		# Return command summary message
		msg = "Delivery stage changed from {} to {}.{}";
		msg = msg.format(stage_old, stage_new, result);
		return msg;

