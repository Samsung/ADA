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
from .User    import User;

class Payment(Base):
	
	__tablename__ = 'Payments';
	__repr_list__ = ("payer", "price", "etofa", "log");
	
	id    = Column(ForeignKey('Summaries.id'), primary_key=True);
	payer = Column(ForeignKey('Users.id'),     nullable=True);
	price = Column(Integer,                    nullable=True);
	etofa = Column(DateTime,                   nullable=True);
	log   = Column(ForeignKey('Logs.id'),      nullable=True);
	
	re_summary = relationship("Summary", backref='Payment');
	re_payer   = relationship("User",    backref='Payment');
	re_log     = relationship("Log",     backref='Payment');
	
	def __init__(self,
			summary : Summary  = None,
			payer   : User     = None,
			price   : int      = None,
			etofa   : datetime = None,
			log     : Log      = None):
		self.re_summary = summary;
		self.re_payer   = payer;
		self.price      = price;
		self.etofa      = etofa;
		self.re_log     = log;
	
	def set_etofa(self,
			etofa : str):
		
		if not etofa:
			self.etofa = None;
			return;
		
		# Validating etofa string
		if not re.search('^[0-2][0-9]:[0-6][0-9]$', etofa):
			msg = 'String {} is not a correct ETofA!';
			msg = msg.format(etofa);
			raise ValueError(etofa);
		
		# Create datetime object from string
		etofa  = etofa.split(':');
		hour   = int(etofa[0]);
		minute = int(etofa[1]);
		etofa  = datetime.datetime.now();
		etofa  = etofa.replace(hour=hour, minute=minute, second=0, microsecond=0);
		
		# Change current etofa
		self.etofa = etofa;
		
		return self;

