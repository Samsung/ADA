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

class Log(Base):
	
	__tablename__ = 'Logs';
	__repr_list__ = ("date", "sender", "receiver", "channel", "content",
	                 "is_input", "delivery");
	
	id       = Column(Integer,  primary_key=True);
	date     = Column(DateTime, nullable=False, default=datetime.now);
	sender   = Column(Integer,  nullable=False);
	receiver = Column(Integer,  nullable=True);
	channel  = Column(String,   nullable=True);
	content  = Column(String,   nullable=False);
	is_input = Column(Boolean,  nullable=False);
	delivery = Column(Integer,  nullable=True);
	
	def __init__(self,
			date     : datetime = None,
			sender   : int      = None,
			receiver : int      = None,
			channel  : str      = None,
			content  : str      = None,
			is_input : bool     = None,
			delivery : int      = None):
		self.date     = date;
		self.sender   = sender;
		self.receiver = receiver;
		self.channel  = channel;
		self.content  = content;
		self.is_input = is_input;
		self.delivery = delivery;

