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

class User(Base):
	
	def init(self):
		self.repo = self.database.repos.users;
	
	def change_role(self,
			user : ada.entities.User,
			role : ada.entities.Role,
			log  : ada.entities.Log):
		
		if user.role == ada.entities.Role.ROOT:
			msg = "The ROOT role cannot be pick up directly!";
			raise ValueError(msg);
		
		if role == ada.entities.Role.ROOT:
			msg = "The ROOT role cannot be changed directly!";
			raise ValueError(msg);
		
		if role == ada.entities.Role.DELETED:
			msg = "Deleting accounts are not implemented yet.";
			raise NotImplementedError(msg);
		
		# Change user role
		user.role        = role;
		user.re_log_role = log;
		
		# Return user
		return user;
	
	def change_root(self,
			user : ada.entities.User,
			log  : ada.entities.Log):
		
		raise NotImplementedError();
	
	def accept(self,
			user : ada.entities.User,
			log  : ada.entities.Log):
		
		if user.role != ada.entities.Role.UNACCEPTED:
			msg = "This is not a new user!";
			raise Exception(msg);
		
		# Accept user account
		user.role        = ada.entities.Role.REGULAR;
		user.re_log_role = log;
		
		# Return user
		return user;
	
	def register(self,
			did  : int,
			nick : str,
			log  : ada.entities.Log):
		
		# Parse argument with user nick
		regex = "^[a-zA-Z0-9_.-]{3,}$";
		if not re.match(regex, nick):
			msg = "This nick is incorrect, it is not matching to this regex {}.";
			msg = msg.format(regex);
			raise ValueError(msg);
		
		# Check if a user with this discord id already exists
		if self.repo.get_one(did=did):
			msg = "Discord id {} already exists!";
			msg = msg.format(did);
			raise ValueError(msg);
		
		# Check if a user with this nick already exists
		if self.repo.get_one(nick=nick):
			msg = "Nick {} already exists!";
			msg = msg.format(nick);
			raise ValueError(msg);
		
		# Set default privilege role based on number of users
		count = self.database.repos.users.query().count();
		role  = ada.entities.Role.ROOT if count<1 else None;
		
		# Create new user
		user = ada.entities.User(did, nick, role, log, log, log);
		self.database.session.add(user);
		
		# Return registered user
		return user;
	
	def generate_list(self):
		
		# Create list with users table header
		headers = ["Id", "Did", "Nick", "Role", "Created", "Action"];
		
		# Get list of all users
		users = self.database.repos.users.get_all();
		
		# Create list with all users data
		rows = [[
			user.id,
			user.did,
			user.nick,
			user.role.name,
			user.re_log_created.date.strftime("%Y-%m-%d %H:%M"),
			user.re_log_action.date.strftime("%Y-%m-%d %H:%M")]
		for user in users if user.role != ada.entities.Role.DELETED];
		
		# Return name of created user
		return (headers, rows);
	
	def set_nick(self, user, nick):
		
		# Parse user nick
		regex = "^[a-zA-Z0-9_.-]{3,}$";
		if not re.match(regex, nick):
			msg = "This nick is incorrect, it is not matching to this regex {}.";
			msg = msg.format(regex);
			raise ValueError(msg);
		
		# Check if nicks are equal
		if user.nick == nick:
			msg = "Old nick and new nick have to be different!"
			raise ValueError(msg);
		
		# Check is nick in use
		if self.database.repos.users.get_one(nick=nick):
			msg = "This nick is already in use!";
			raise ValueError(msg);
		
		# Change current nick
		user.nick = nick;

