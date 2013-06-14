#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Path to scan file
scan = 'scan.txt'

# Path to database export file
baza = 'baza.txt'

res = set(open(scan)).difference(set(open(baza)))

for x in res:
    print x.strip()
