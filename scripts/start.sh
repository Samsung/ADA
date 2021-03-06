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

# Read environment configuration name
env="$1";

# Check if environment configuration exists
if [   -z "$env" ] \
|| [ ! -d "confs/$env" ] \
|| [   -f "confs/$env/lock" ]
then
	echo "There is some error with environment configuration!";
	exit 1;
fi

# Create safety lock file.
touch "confs/$env/lock";

# Start container using selected environment configuration
docker run -it \
	--detach \
	--restart  always \
	--name     "ada-$env" \
	--env-file "$PWD/confs/$env/env.conf" \
	--volume   "$PWD/confs/$env/database.sqlite:/var/lib/ada/database.sqlite" \
	"${@:2}" "samsung/kot/ada:$env";

