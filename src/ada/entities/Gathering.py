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
from .Delivery import Delivery;

class Gathering(Base):
	
	__tablename__ =  "Gatherings";
	__repr_list__ = ("started", "timeout", "ended");
	
	id      = Column(ForeignKey('Deliveries.id'), primary_key=True);
	started = Column(DateTime,                    nullable=False, default=datetime.now);
	timeout = Column(DateTime,                    nullable=True);
	ended   = Column(DateTime,                    nullable=True);
	
	re_delivery   = relationship("Delivery",  backref='Gathering');
	re_voting     = relationship("Voting",    back_populates="re_gathering", uselist=False);
	re_candidates = relationship("Candidate", back_populates="re_gathering");
	
	def __init__(self,
			delivery : Delivery = None,
			started  : datetime = None,
			timeout  : datetime = None,
			ended    : datetime = None):
		self.re_delivery = delivery;
		self.started     = started;
		self.timeout     = timeout;
		self.ended       = ended;

