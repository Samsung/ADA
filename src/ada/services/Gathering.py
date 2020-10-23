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

class Gathering(Base):
	
	def init(self):
		self.repo = self.database.repos.gatherings;
	
	def status(self):
		
		delivery   = self.repos.deliveries.get_current();
		candidates = delivery.re_gathering.re_candidates;
		names      = list();
		
		for candidate in candidates:
			names.append(candidate.re_restaurant.name);
		
		names    = ', '.join(names);
		header   = 'List of submitted candidates:';
		response = ' '.join([header,names]);
		
		return response;
	
	def next(self):
		
		delivery  = self.repos.deliveries.get_current();
		gathering = delivery.re_gathering;
		status    = self.status();
		
		if len(gathering.re_candidates) < 1:
			msg = 'There is no candidates for voting.';
			raise Exception(msg);
		
		timeout = None # ada.core.Config.timeout('VOTE');
		voting  = ada.entities.Voting(gathering, timeout=timeout);
		delivery.stage = ada.entities.Stage.VOTE;
		self.database.session.add(voting);
		self.database.session.commit();
		
		return status;
	
	def submits(self,
			gathering   : ada.entities.Gathering,
			restaurants : typing.List[ada.entities.Restaurant],
			log         : ada.entities.Log):
		
		# Submit all given restaurants to voting candidates
		candidates = [self.submit(gathering, rest, log) for rest in restaurants];
		
		# Commit database changes
		self.database.session.commit();
		
		# Return submitted candidates
		return candidates;
	
	def rejects(self,
			gathering   : ada.entities.Gathering,
			restaurants : typing.List[ada.entities.Restaurant]):
		
		# Reject all given restaurants from voting candidates
		candidates = [self.reject(gathering, rest) for rest in restaurants];
		
		# Commit database changes
		self.database.session.commit();
		
		# Return rejected candidates
		return candidates;
	
	def submit(self,
			gathering  : ada.entities.Gathering,
			restaurant : ada.entities.Restaurant,
			log        : ada.entities.Log):
		
		# Try to find candidate by gathering and restaurant
		candidate = self.repos.candidates.get_by_gathering_restaurant(gathering, restaurant);
		
		# Test if candidate already exists
		if candidate:
			return candidate;
		
		# Create and save new candidate object
		candidate = ada.entities.Candidate(gathering, restaurant, log);
		self.database.session.add(candidate);
		
		# Return submitted candidate
		return candidate;
	
	def reject(self,
			gathering  : ada.entities.Gathering,
			restaurant : ada.entities.Restaurant):
		
		# Try to find candidate by gathering and restaurant
		candidate = self.repos.candidates.get_by_gathering_restaurant(gathering, restaurant);
		
		# Test if candidate is unique
		if not candidate:
			candidate = ada.entities.Candidate(gathering, restaurant, log);
			return candidate;
		
		# Delete candidate object
		self.database.session.delete(candidate);
		
		# Return rejected candidate
		return candidate;

