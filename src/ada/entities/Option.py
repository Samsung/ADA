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
from .Log  import Log;

class Option(Base):
	
	__tablename__ = 'Options';
	__repr_list__ = ("key", "value", "log");
	
	id    = Column(Integer,               primary_key=True);
	key   = Column(String,                nullable=False, unique=True);
	value = Column(Text,                  nullable=False);
	log   = Column(ForeignKey('Logs.id'), nullable=False);
	
	log_re = relationship("Log", foreign_keys=[log]);
	
	def __init__(self,
			key   : str = None,
			value : str = None,
			log   : Log = None):
		self.key    = key;
		self.value  = value;
		self.log_re = log;

