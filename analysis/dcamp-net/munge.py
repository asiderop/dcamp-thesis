#!/usr/bin/env python3
from sys import argv, stdin
from os.path import basename
from collections import namedtuple
import re

r = re.compile('(\w+)=(\d+),? ?')
T = namedtuple('T', 'ts, b, p')

prev = None
ts = 0
for l in stdin:
    d = dict(r.findall(l))
    b = int(d['bytes_sent']) + int(d['bytes_recv'])
    p = int(d['packets_sent']) + int(d['packets_recv'])
    cur = T(int(d['ts']), b, p)

    if prev is not None:
        t = cur.ts - prev.ts
        ts += t
        bs = (cur.b - prev.b) / t
        ps = (cur.p - prev.p) / t
        print('{},{:.2f},{:.2f}'.format(ts, bs, ps))

    prev = cur

