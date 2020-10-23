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
from .User import User;

class Transfer(Base):
	
	__tablename__ = 'Transfers';
	__repr_list__ = ("date", "sender", "receiver", "amount", "note", "approved",
	                 "log_initial", "log_final");
	
	id          = Column(Integer,                primary_key=True);
	date        = Column(DateTime,               nullable=False, default=datetime.now);
	sender      = Column(ForeignKey('Users.id'), nullable=False);
	receiver    = Column(ForeignKey('Users.id'), nullable=False);
	amount      = Column(Integer,                nullable=False);
	note        = Column(Text,                   nullable=False);
	approved    = Column(Boolean,                nullable=True);
	log_initial = Column(ForeignKey('Logs.id'),  nullable=False);
	log_final   = Column(ForeignKey('Logs.id'),  nullable=True);
	
	re_sender      = relationship("User", foreign_keys=[sender]);
	re_receiver    = relationship("User", foreign_keys=[receiver]);
	re_log_initial = relationship("Log",  foreign_keys=[log_initial]);
	re_log_final   = relationship("Log",  foreign_keys=[log_final]);
	
	def __init__(self,
			date        : datetime = None,
			sender      : User     = None,
			receiver    : User     = None,
			amount      : int      = None,
			note        : str      = None,
			approved    : bool     = None,
			log_initial : Log      = None,
			log_final   : Log      = None):
		self.date           = date;
		self.sender_re      = sender;
		self.receiver_re    = receiver;
		self.amount         = amount;
		self.note           = note;
		self.approved       = approved;
		self.re_log_initial = log_initial;
		self.re_log_final   = log_final;

