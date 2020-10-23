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

# Change working directory to project directory
cd "$(dirname "${BASH_SOURCE[0]}")/..";

# Add src directory to python modules path
export PYTHONPATH="$PYTHONPATH:$PWD/src";

# Execute tests selected by regex and calculate coverage
find tests -type f -iname \*.py -print0 | grep -zEe "$1" |\
xargs -0 python3 -B -m pytest -p no:cacheprovider -s -r s \
--verbosity=2 --durations=4 --no-cov-on-fail --cov=ada \
--cov-report term-missing:skip-covered "--";

# Remove coverage cache
rm -f .coverage;

