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

class Votings(Base):
	"""
		Repository class for Voting entity.
	"""
	
	entity = entities.Voting;
	
	def generate_values(self, voting):
		
		# TODO: If possible refactor this to SQLAlchemy queries.
		
		# Create dict for values
		values = dict();
		
		# For every vote in this voting
		for vote in voting.re_votes:
			
			# Add new dict for user if not exists
			user = vote.re_voter.nick;
			if user not in values:
				values[user] = dict();
			
			# Add vote value to user dict
			name = vote.re_candidate.re_restaurant.name;
			values[user][name] = vote.value;
		
		# Return summary as tuple
		return values;
	
	def generate_summary(self, voting):
		
		# TODO: If possible refactor this to SQLAlchemy queries.
		
		# Create dict for summary
		summary = dict();
		
		# Initialize summary dict
		for candidate in voting.re_gathering.re_candidates:
			name = candidate.re_restaurant.name;
			summary[name] = 0;
		
		# For every vote in this voting
		for vote in voting.re_votes:
			
			# Get name of restaurant from current vote
			name = vote.re_candidate.re_restaurant.name;
			
			# Add vote value to restaurant values
			summary[name] += vote.value;
		
		# Return summary dict
		return summary;

