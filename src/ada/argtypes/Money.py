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

class Money(Base):
	"""
		Class to validate and convert money string into integer value.
	"""
	
	VALUE_MIN  = -100000000;
	VALUE_MAX  =  100000000;
	VALUE_MUL =         100;
	
	REGEX_FIRST =  r"[ ]*[+-]{0,1}[ ]*(0|[1-9][0-9]*)(\.[0-9]{1,2})?[ ]*";
	REGEX_NEXT  =  r"[ ]*[+-]{1,1}[ ]*(0|[1-9][0-9]*)(\.[0-9]{1,2})?[ ]*";
	REGEX_FULL  = fr"^({REGEX_FIRST})({REGEX_NEXT})*$"
	
	def call(self,
			value : str)\
			-> int:
		
		if not re.match(self.REGEX_FULL, value):
			msg = "Money value has to match to this input filter: {} !";
			msg = msg.format(self.REGEX_FULL);
			raise ArgumentTypeError(msg);
		
		value   = value.strip();
		value   = value.replace(" ", "");
		value   = value.replace("+", "\n+");
		value   = value.replace("-", "\n-");
		numbers = value.splitlines();
		numbers = numbers if numbers[0] else numbers[1:];
		numbers = [self.parse(number) for number in numbers];
		result  = sum(numbers);
		
		if result < self.VALUE_MIN or self.VALUE_MAX < result:
			msg = "Money only supports values from {} to {}!";
			msg = msg.format(self.VALUE_MIN, self.VALUE_MAX);
			raise ArgumentTypeError(msg);
		
		return result;
	
	def parse(self, value_str : str) -> int:
		
		try:
			value_float = float(value_str);
			value_float = round(value_float, 2);
		except ArgumentTypeError:
			msg = "Money value should be convertible to float value!";
			raise ArgumentTypeError(msg);
		
		value_int = int(round(self.VALUE_MUL*value_float, 2));
		
		if value_float != value_int/self.VALUE_MUL:
			msg = "Maximum granulation for money type is 0.01!";
			raise ArgumentTypeError(msg);
		
		if value_int < self.VALUE_MIN or self.VALUE_MAX < value_int:
			msg = "Money only supports values from {} to {}!";
			msg = msg.format(self.VALUE_MIN, self.VALUE_MAX);
			raise ArgumentTypeError(msg);
		
		return value_int;
	
	def format(self,
			value : int)\
			-> str:
		
		if value < self.VALUE_MIN or self.VALUE_MAX < value:
			msg = "The MoneyType only supports values from {} to {}!";
			msg = msg.format(self.VALUE_MIN, self.VALUE_MAX);
			raise ArgumentTypeError(msg);
		
		absolute  = abs(value);
		prefix    = "-" if value < 0 else "";
		integer   = absolute // self.VALUE_MUL;
		fraction  = absolute %  self.VALUE_MUL;
		formatted = f"{prefix}{integer}.{fraction:02d}";
		
		return formatted;

