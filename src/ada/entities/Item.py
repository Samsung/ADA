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

from .Base  import *;
from .Log   import Log;
from .Order import Order;
from .User  import User;

class Item(Base):
	
	__tablename__ = 'Items';
	__repr_list__ = ("order", "purchaser", "price", "note", "log");
	
	id        = Column(Integer,                 primary_key=True);
	order     = Column(ForeignKey('Orders.id'), nullable=False);
	purchaser = Column(ForeignKey('Users.id'),  nullable=False);
	price     = Column(Integer,                 nullable=False);
	note      = Column(String,                  nullable=False);
	log       = Column(ForeignKey('Logs.id'),   nullable=False);
	
	re_order     = relationship("Order", foreign_keys=[order]);
	re_purchaser = relationship("User",  foreign_keys=[purchaser]);
	re_log       = relationship("Log",   foreign_keys=[log]);
	
	def __init__(self,
			order     : Order = None,
			purchaser : User  = None,
			price     : int   = None,
			note      : str   = None,
			log       : Log   = None):
		self.re_order     = order;
		self.re_purchaser = purchaser;
		self.price        = price;
		self.note         = note;
		self.re_log       = log;

