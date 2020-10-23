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

class Restaurant(Base):
	
	def init(self):
		self.repo = self.database.repos.restaurants;
	
	def create(self,
			key  : str,
			name : str,
			url  : str,
			log  : ada.entities.Log):
		
		# Make sure, that restaurant is unique
		if self.repo.get_one(key=key):
			msg = f"Restaurant with key {key} already exists!";
			raise ValueError(msg);
		elif self.repo.get_one(name=name):
			msg = f"Restaurant with name {name} already exists!";
			raise ValueError(msg);
		elif url and self.repo.get_one(url=url):
			msg = f"Restaurant with URL {url} already exists!";
			raise ValueError(msg);
		
		# Create and add to database new restaurant
		restaurant = ada.entities.Restaurant(key, name, url, True, log, log);
		self.database.session.add(restaurant);
		
		# Return created restaurant
		return restaurant;
	
	def update(self,
			restaurant,
			field,
			value,
			log):
		
		setattr(restaurant, field, value);
		self.database.session.commit();
		
		return restaurant;
	
	def delete(self,
			restaurant : ada.entities.Restaurant,
			log        : ada.entities.Log):
		
		if restaurant.re_candidates:
			msg = "The restaurant cannot be deleted,"\
			      " but you can try to deactivate it instead.";
			raise ValueError(msg);
		
		self.database.session.delete(restaurant);
		
		return restaurant;
	
	def listing(self,
			inactive : bool = False)\
			-> object:
		
		# Create list with users table header
		header = ['Id', 'Key', 'Name', 'Url', "Active"];
		
		# Get list of all users
		restaurants = self.database.repos.restaurants.get_all();
		
		# Create list with all users data
		rows = [[
			restaurant.id,
			restaurant.key,
			restaurant.name,
			restaurant.url,
			restaurant.active]
			for restaurant in restaurants
			if restaurant.active
			or (restaurant.active != inactive)
		];
		
		# Return name of created user
		return (header, rows);

