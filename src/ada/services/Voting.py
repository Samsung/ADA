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

class Voting(Base):
	
	def init(self):
		self.repo = self.repos.votings;
	
	def status(self):
		
		delivery   = self.repos.deliveries.get_current();
		gathering  = delivery.re_gathering;
		voting     = gathering.re_voting;
		candidates = gathering.re_candidates;
		
		# Create variables for table generating
		header = ['User'    ];
		footer = ['Summary:'];
		rows   = list();
		
		# Get voting values and summary
		values  = self.repo.generate_values(voting);
		summary = self.repo.generate_summary(voting);
		
		# Initialize header and footer
		for candidate in candidates:
			name = candidate.re_restaurant.name;
			header.append(name);
			footer.append(summary[name]);
		
		# Generate table rows
		for user,votes in values.items():
			row = [user];
			for candidate in candidates:
				name  = candidate.re_restaurant.name;
				value = votes[name];
				row.append(value);
			rows.append(row);
		
		# Add row with summary
		rows.append('');
		rows.append(footer);
		
		# Generate ascii table with results
		table = str(tabulate.tabulate(rows, header, tablefmt="simple"));
		table = "```\n{}\n```".format(table);
		
		# Return results table
		return table;
	
	def vote(self, user, votes, log):
		
		delivery   = self.repos.deliveries.get_current();
		gathering  = delivery.re_gathering;
		voting     = gathering.re_voting;
		candidates = gathering.re_candidates;
		size       = len(candidates);
		
		if len(votes) != size:
			msg = 'The number of candidates and the number of votes are not equal!';
			raise ValueError(msg);
		
		for index in range(size):
			candidate = candidates[index];
			value = int(votes[index]);
			
			if value < 0:
				msg = 'Vote value is too low, minimum vote value is 0!';
				raise ValueError(msg);
			
			if value > 10:
				msg = 'Vote value is too high, minimum vote value is 10!';
				raise ValueError(msg);
			
			self.repos.votes.create_or_update(voting, user, candidate, value, log);
		
		self.database.session.commit();
	
	def next(self):
		
		delivery   = self.repos.deliveries.get_current();
		gathering  = delivery.re_gathering;
		voting     = gathering.re_voting;
		
		# Get voting status table
		table = self.status();
		
		# Get voting summary
		summary = self.repo.generate_summary(voting);
		
		# Find maximum points for candidate in this voting
		maximum_points = max(summary.values());
		
		# Get names of voting winners
		winners = [k for k,v in summary.items() if v == maximum_points];
		
		# If there is more than one winner
		if len(winners) > 1:
			msg = table + 'There is more than one winner, vote again!';
			raise Exception(msg);
		
		# Save winner name
		winner_name = winners[0];
		
		# Get object of voting winner
		winner = self.repos.gatherings.get_candidate_by_name(gathering, winner_name);
		
		# Save voting winner
		voting.re_winner = winner;
		
		# Create new order
		timeout = None; # ada.core.Config.timeout('ORDER');
		order   = ada.entities.Order(voting, timeout=timeout);
		
		# Change delivery stage
		delivery.stage = ada.entities.Stage.ORDER;
		
		# Commit all changes
		self.database.session.add(order);
		self.database.session.commit();
		
		# Generate message with winner name
		message = "{}\nVoting winner is {} (`{}`)";
		message = message.format(table, winner_name, winner.re_restaurant.url);
		
		# Return winner name
		return message;

