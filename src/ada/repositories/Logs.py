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

class Logs(Base):
	
	entity = entities.Log;
	
	def create_from_message(self, sender, receiver, channel, content, is_input, delivery):
		try:
			# Create, save and return new log object
			delivery_id = None if not delivery else delivery.id;
			log = self.entity(None, sender, receiver, channel, content, is_input, delivery_id);
			self.session.add(log);
			self.session.commit();
			return log;
			
		except Exception as e:
			print(e)
			# Throw exception in case of error
			msg = 'Error while creating a log!';
			raise Exception(msg) from e;

