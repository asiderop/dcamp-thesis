#!/usr/bin/env python3.3

import time
import psutil

while True:
  net = vars(psutil.net_io_counters())
  s = 'ts={}'.format(int(round(time.time())))
  for (k,v) in net.items():
    s += ', {}={}'.format(k, v)
  print(s)
  time.sleep(10)

