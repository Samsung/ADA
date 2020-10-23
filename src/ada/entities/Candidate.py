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

from .Base       import *;
from .Log        import Log;
from .Gathering  import Gathering;
from .Restaurant import Restaurant;

class Candidate(Base):
	
	__tablename__  = 'Candidates';
	__repr_list__  = ("gathering", "restaurant", "log");
	__table_args__ = (UniqueConstraint('gathering', 'restaurant'),);
	
	id         = Column(Integer,                      primary_key=True);
	gathering  = Column(ForeignKey('Gatherings.id'),  nullable=False);
	restaurant = Column(ForeignKey('Restaurants.id'), nullable=False);
	log        = Column(ForeignKey('Logs.id'),        nullable=False);
	
	re_gathering  = relationship("Gathering",  backref='Candidate');
	re_restaurant = relationship("Restaurant", backref='Candidate');
	re_log        = relationship("Log",        backref='Candidate');
	re_votes      = relationship("Vote",       back_populates="re_candidate");
	
	def __init__(self,
			gathering  : Gathering  = None,
			restaurant : Restaurant = None,
			log        : Log        = None):
		self.re_gathering  = gathering;
		self.re_restaurant = restaurant;
		self.re_log        = log;

