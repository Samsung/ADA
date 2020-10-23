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

class Restaurant(Base):
	
	__tablename__ = 'Restaurants';
	__repr_list__ = ("key", "name", "url", "active", "log_created", "log_action");
	
	id          = Column(Integer,               primary_key=True);
	key         = Column(String,                nullable=False, unique=True);
	name        = Column(String,                nullable=False, unique=True);
	url         = Column(String,                nullable=True,  unique=True);
	active      = Column(Boolean,               nullable=False, default=False);
	log_created = Column(ForeignKey('Logs.id'), nullable=False);
	log_action  = Column(ForeignKey('Logs.id'), nullable=False);
	
	re_log_created = relationship("Log", foreign_keys=[log_created]);
	re_log_action  = relationship("Log", foreign_keys=[log_action]);
	re_candidates  = relationship("Candidate", back_populates="re_restaurant");
	
	def __init__(self,
			key         : str  = None,
			name        : str  = None,
			url         : str  = None,
			active      : bool = None,
			log_created : Log  = None,
			log_action  : Log  = None):
		self.key            = key;
		self.name           = name;
		self.url            = url;
		self.active         = active;
		self.re_log_created = log_created;
		self.re_log_action  = log_action;

