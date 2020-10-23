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

class Management(Base):
	
	def get_service(self,
			services,
			stage)\
			-> object:
		"""
			Get service by stage name
		"""
		
		# Map stages to services
		stages_mapping = {
			ada.entities.Stage.SLEEP   : "sleep",
#			ada.entities.Stage.INIT    : None,
			ada.entities.Stage.GATHER  : "gathering",
			ada.entities.Stage.VOTE    : "voting",
			ada.entities.Stage.ORDER   : "order",
			ada.entities.Stage.SUMMARY : "summary",
			ada.entities.Stage.ADJUST  : "adjustment",
#			ada.entities.Stage.CANCEL  : None,
#			ada.entities.Stage.FINISH  : None,
		};
		
		# Test if stage can be mapped to service
		if stage not in stages_mapping:
			msg = 'Stage {} can not be mapped to service!';
			msg = msg.format(stage);
			raise KeyError(msg);
		
		# Get service by stage name
		attr = stages_mapping[stage];
		service = getattr(services, attr);
		
		# Return service
		return service;

