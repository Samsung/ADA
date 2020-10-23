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

import re;
import typing;

class Formatter(Base):
	"""
		Prepare discord message content to be send.
		Split it into smaller pieces and escape some special characters.
		TODO: This feature may not work properly in some cases!
	"""
	
	def __init__(self, *args, **kwargs):
		
		super().__init__(*args, **kwargs);
		
		self.limit = self.arguments.limit;
	
	def __call__(self, content:str) -> typing.List[str]:
		
		# Message length limit cannot be too small
		if self.limit < 64:
			msg = "Message limit is too small!";
			raise Exception(msg);
		
		# If there is not content, then return empty list
		if content is None:
			return [];
		
		# Prepare monospace block magic sequences
		magic  = "```";
		prefix = "```\n";
		middle = "\n```\n";
		suffix = "\n```";
		
		# Make sure that monospace block magic sequence
		# is always the only characters in line
		content = re.sub("\n?```\n?", middle, content);
		content = content[1:  ] if content.startswith(middle) else content;
		content = content[ :-1] if content.endswith(  middle) else content;
		
		# Split message content into lines
		lines = content.splitlines();
		
		# Replace lines that are too long
		error = "This line was too long and has been replaced!";
		lines = [line if len(line) <= self.limit else error for line in lines];
		
		# Calculate length of each next line
		len_next = [len(line) for line in lines];
		len_next = len_next[1:] + [self.limit];
		
		# Are we currently in monospace block?
		ismono = 0;
		
		# Find lines that should be escaped
		for line in lines:
			
			# Check if we are in monospace block
			if line == magic:
				ismono = not ismono;
			
			# Do not escape in monospace block
			if ismono:
				continue;
			
			# Escape monospace inline magic sequences
			line = re.sub("^`[^`]",    "\\`", line);
			line = re.sub("[^`]`[^`]", "\\`", line);
			line = re.sub("[^`]`$",    "\\`", line);
		
		# Temporary variables
		pieces = []; # List to storage message content pieces
		buffer = []; # List to storage current piece lines
		size   = 0;  # Current piece buffer size
		ismono = 0;  # Are we in monospace block?
		
		# For each line in message content
		for i,line in enumerate(lines):
			
			# Check if we are in monospace block
			if line == magic:
				ismono = not ismono;
			
			# Add line to buffer
			buffer.append(line);
			size += len(line);
			
			# If we do not have too much in buffer,
			# then add to bufffer next line
			if size + len(buffer) + len_next[i] < self.limit:
				continue;
			
			# Join lines into text
			buffer = "\n".join(buffer);
			buffer = buffer+suffix if ismono else buffer;
			
			# Save text
			pieces.append(buffer);
			
			# Start new piece
			buffer  = [magic]    if ismono else [];
			size    = len(magic) if ismono else 0;
		
		# Return pieces
		return pieces;

