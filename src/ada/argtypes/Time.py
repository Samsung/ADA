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
import datetime;

class Time(Base):
	
	def call(self,
			value : str)\
			-> datetime.datetime:
		
		regex = r"^([0-2]?[0-9]):([0-6][0-9])$";
		match = re.search(regex, value);
		
		if not match:
			msg = "Invalid time string format {}, required format is HH:MM.";
			msg = msg.format(value);
			raise ArgumentTypeError(msg);
		
		hour_str   = match.group(1);
		minute_str = match.group(2);
		
		try:
			hour   = int(hour_str);
			minute = int(minute_str);
		except ValueError:
			msg = "Invalid hour or minute number!";
			raise ArgumentTypeError(msg);
		
		time = datetime.datetime.now();
		time = time.replace(hour=hour, minute=minute, second=0, microsecond=0);
		
		return time;

