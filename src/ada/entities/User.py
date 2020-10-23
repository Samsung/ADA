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
from .Role import Role;
from .Log  import Log;

class User(Base):
	
	__tablename__ = 'Users';
	__repr_list__ = ("did", "nick", "role", "log_created", "log_action", "log_role");
	
	id          = Column(Integer,               primary_key=True);
	did         = Column(Integer,               nullable=False, unique=True);
	nick        = Column(String,                nullable=False, unique=True);
	role        = Column(Enum(Role),            nullable=False, default=Role.UNACCEPTED);
	log_created = Column(ForeignKey('Logs.id'), nullable=False);
	log_action  = Column(ForeignKey('Logs.id'), nullable=False);
	log_role    = Column(ForeignKey('Logs.id'), nullable=False);
	
	re_log_created = relationship("Log", foreign_keys=[log_created]);
	re_log_action  = relationship("Log", foreign_keys=[log_action]);
	re_log_role    = relationship("Log", foreign_keys=[log_role]);
	
	def __init__(self,
			did         : int  = None,
			nick        : str  = None,
			role        : Role = None,
			log_created : Log  = None,
			log_action  : Log  = None,
			log_role    : Log  = None):
		self.did            = did;
		self.nick           = nick;
		self.role           = role;
		self.re_log_created = log_created;
		self.re_log_action  = log_action;
		self.re_log_role    = log_role;
	
	@property
	def mention(self):
		
		if self.did is None:
			return None;
		
		return f"<@{self.did}>";

