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

from .Base   import *;
from .Voting import Voting;

class Order(Base):
	
	__tablename__ = 'Orders';
	__repr_list__ = ("started", "timeout", "ended");
	
	id      = Column(ForeignKey('Votings.id'), primary_key=True);
	started = Column(DateTime,                 nullable=False, default=datetime.now);
	timeout = Column(DateTime,                 nullable=True);
	ended   = Column(DateTime,                 nullable=True);
	
	re_voting  = relationship("Voting",  backref='Order');
	re_summary = relationship("Summary", back_populates="re_order", uselist=False);
	re_items   = relationship("Item",    back_populates="re_order");
	
	def __init__(self,
			voting  : Voting   = None,
			started : datetime = None,
			timeout : datetime = None,
			ended   : datetime = None):
		self.re_voting = voting;
		self.started   = started;
		self.timeout   = timeout;
		self.ended     = ended;

