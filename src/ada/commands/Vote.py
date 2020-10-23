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

class Vote(Base):
	
	name   = 'vote';
	help   = 'Vote for the candidates in VOTE stage.';
	exce   = "Error while voting for restaurants";
	role   = ada.entities.Role.REGULAR;
	stages = ada.entities.Stage.VOTE;
	
	def init(self):
		
		self.add_argument("votes",
			nargs   = "+",
			type    = int,
			choices = range(0, 11),
			metavar = "vote",
			help    = "Vote for restaurants submitted in gathering stage,"\
			          " allowed values from 0 to 10.");
	
	def exec(self, whoami, author, channel, content, argv, args, log, user, delivery):
		
		# Create useful aliases
		votes = args.votes;
		
		# Vote in the current voting
		self.services.voting.vote(user, votes, log);
		
		# Return command summary message
		msg = "Your vote has been saved.";
		return msg;

