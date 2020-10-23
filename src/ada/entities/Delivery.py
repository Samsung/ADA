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

from .Base    import *;
from .Log     import Log;
from .Stage   import Stage;

class Delivery(Base):
	
	__tablename__ = "Deliveries";
	__repr_list__ = ("started", "stage", "ignored", "ended", "log_start",
	                 "log_end");
	
	id        = Column(Integer,               primary_key=True);
	started   = Column(DateTime,              nullable=False, default=datetime.now);
	stage     = Column(Enum(Stage),           nullable=False, default=Stage.INIT);
	ignored   = Column(Boolean,               nullable=False, default=False, index=True);
	ended     = Column(DateTime,              nullable=True,                 index=True);
	log_start = Column(ForeignKey('Logs.id'), nullable=False);
	log_end   = Column(ForeignKey('Logs.id'), nullable=True);
	
	re_log_start = relationship("Log", foreign_keys=[log_start]);
	re_log_end   = relationship("Log", foreign_keys=[log_end]);
	re_gathering = relationship("Gathering", back_populates="re_delivery", uselist=False);
	
	def __init__(self,
			started   : datetime = None,
			stage     : Stage    = None,
			ignored   : bool     = None,
			ended     : datetime = None,
			log_start : Log      = None,
			log_end   : Log      = None):
		self.started      = started;
		self.stage        = stage;
		self.ignored      = ignored;
		self.ended        = ended;
		self.re_log_start = log_start;
		self.re_log_end   = log_end;

