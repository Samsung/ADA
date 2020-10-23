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

class Stage(enum.Enum):
	"""
		List of stages names in which program/delivery can be.
		Documentation for stages is in docs/stages.md file.
		This entity does not have representation in database!
	"""
	
	SLEEP   = 'SLEEP';   # Waiting for delivery start
	INIT    = 'INIT';    # Delivery created, but not ready yet
	GATHER  = 'GATHER';  # Gathering restaurants for voting
	VOTE    = 'VOTE';    # Voting for restaurant
	ORDER   = 'ORDER';   # Ordering from restaurant which win voting
	SUMMARY = 'SUMMARY'; # Summarizing order and waiting for delivery
	ADJUST  = 'ADJUST';  # Correction of order after delivery
	FINISH  = 'FINISH';  # Delivery was finished and is in history
	CANCEL  = 'CANCEL';  # Delivery was canceled and is ignored

