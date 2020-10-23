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

class Votes(Base):
	"""
		Basic repository class for Vote entity.
	"""
	
	entity = ada.entities.Vote;
	
	def create_or_update(self, voting, voter, candidate, value, log):
		
		# Find existing vote
		vote = self.get_one(
			re_voting    = voting,
			re_voter     = voter,
			re_candidate = candidate);
		
		if not vote:
			vote = ada.entities.Vote(voting, voter, candidate, value, log);
			self.session.add(vote);
		
		vote.value  = value;
		vote.re_log = log;
		
		return vote;

