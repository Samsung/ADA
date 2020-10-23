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

from .Base      import *;
from .Log       import Log;
from .Candidate import Candidate;
from .User      import User;
from .Voting    import Voting;

class Vote(Base):
	
	__tablename__  =  "Votes";
	__repr_list__  = ("voting", "voter", "candidate", "value", "log");
	__table_args__ = (UniqueConstraint('voting', 'voter', 'candidate'),);
	
	id        = Column(Integer,                     primary_key=True);
	voting    = Column(ForeignKey('Votings.id'),    nullable=False);
	voter     = Column(ForeignKey('Users.id'),      nullable=False);
	candidate = Column(ForeignKey('Candidates.id'), nullable=False);
	value     = Column(Integer,                     nullable=False);
	log       = Column(ForeignKey('Logs.id'),       nullable=False)
	
	re_voting    = relationship("Voting",    backref='Vote');
	re_voter     = relationship("User",      backref='Vote');
	re_candidate = relationship("Candidate", backref='Vote');
	re_log       = relationship("Log",       backref='Vote');
	
	def __init__(self,
			voting    : Voting    = None,
			voter     : User      = None,
			candidate : Candidate = None,
			value     : int       = None,
			log       : Log       = None):
		self.re_voting    = voting;
		self.re_voter     = voter;
		self.re_candidate = candidate;
		self.value        = value;
		self.re_log       = log;

