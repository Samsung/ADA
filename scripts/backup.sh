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

# Save environment from script argument
env="$(basename -- "$1")";

# Generate required paths
conf="confs/$env";
yaml="$conf/config.yaml";
data="$conf/database.sqlite";

# Check environment name and required paths
[   -z "$env"  ] && echo "Environment name is required as first argument!"  && exit 1;
[ ! -d "$conf" ] && echo "Configuration directory ($conf) does not exists!" && exit 2;
[ ! -f "$yaml" ] && echo "Configuration file ($conf) does not exists!"      && exit 3;
[ ! -f "$data" ] && echo "Database file ($conf) does not exists!"           && exit 4;

# Generate backup name and path
base="ada-backup-$env";
date="$(date +%F\ %T)";
name="$base ($date)";
path="backups/$name";

# Create directory for backup files
mkdir -p "$path";

# Make sure that directory for new backup exists
[ ! -d "$path" ] && echo "New backup directory does not exists!" && exit 5;

# Copy configuration and database to backup directory
cp "$yaml" "$path/config.yaml";
cp "$data" "$path/database.sqlite";

# Save backup name
echo "$name" > "$path/name.txt";

# Generate database dump and add it into backup
sqlite3 "$data" .dump > "$path/database.sql";

# Save informations about repository
git log -n 1 > "$path/git-log.txt";
git status   > "$path/git-status.txt";
git diff     > "$path/git-diff.txt";

# Go to backups directory
cd "backups";

# Create checksums for this backup
find "$name" -type f -not -name sha1sum -print0 |\
sort -z | xargs --null sha1sum -- | tee "$name/sha1sum";

# Create backup archive
zip -r "$name.zip" "$name";

