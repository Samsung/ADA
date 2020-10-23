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
from .Summary import Summary;

class Adjustment(Base):
	
	__tablename__ = 'Adjustments';
	__repr_list__ = ("started", "ended", "log");
	
	id      = Column(ForeignKey('Summaries.id'), primary_key=True);
	started = Column(DateTime,                   nullable=False, default=datetime.now);
	ended   = Column(DateTime,                   nullable=True);
	log     = Column(ForeignKey('Logs.id'),      nullable=True);
	
	re_summary     = relationship("Summary",    foreign_keys=[id]);
	re_log         = relationship("Log",        foreign_keys=[log]);
	re_corrections = relationship("Correction", back_populates="re_adjustment");
	
	def __init__(self,
			summary : Summary  = None,
			started : datetime = None,
			ended   : datetime = None,
			log     : Log      = None):
		self.re_summary = summary;
		self.started    = started;
		self.ended      = ended;
		self.re_log     = log;

