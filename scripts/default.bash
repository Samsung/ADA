#! /bin/bash

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

# Change current directory to root directory
cd "$(dirname "${BASH_SOURCE[0]}")/..";

# Test if there is configuration file
if [ ! -f "$1" ]
then
	echo Configuration file should be given as first argument of this script;
	exit 1;
fi

# Load configuration variables
source "$1";

# Test for all needed exports
[ -z "$ENV"      ] && echo Export ENV      variable! && exit 1;
[ -z "$CHANNEL"  ] && echo Export CHANNEL  variable! && exit 2;
[ -z "$TOKEN"    ] && echo Export TOKEN    variable! && exit 3;
[ -z "$DATABASE" ] && echo Export DATABASE variable! && exit 4;
[ -z "$LOG"      ] && echo Export LOG      variable! && exit 5;
[ -z "$LOCK"     ] && echo Export LOCK     variable! && exit 6;

# Kill all old ada instances
killall python3;
sleep 1s;

# Start new ada instance
bash scripts/run.bash      \
	--env      "$ENV"      \
	--channel  "$CHANNEL"  \
	--token    "$TOKEN"    \
	--database "$DATABASE" \
	--log      "$LOG"      \
	--lock     "$LOCK"     \
	--debug;

