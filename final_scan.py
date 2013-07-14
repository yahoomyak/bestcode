#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# ~$ python cmp.py > result_id.txt
id = [x.strip() for x in open('result_id.txt')]

# baza.txt - 1c export
raw = [x for x in open('baza.txt')][4:] 

res = [x for x in raw if x.split(' ', 1)[0] in id]

for x in res:
    print x
