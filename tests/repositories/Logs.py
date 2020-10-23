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


import ada;

def test(database, match):
	
	repo = ada.repositories.Logs(database.session);
	log  = repo.create_from_message(1, 2, "channel", "content", 1, None);
	logs = repo.get_all();
	
	assert len(logs) == 1;
	assert match(r"Log\(id=1, date=202.*, sender=1, receiver=2, channel=channel, content=content, is_input=True, delivery=None\)", logs[0]);

