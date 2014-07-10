#!/usr/bin/env python3

from time import time, sleep
import psutil

from sys import argv
from os.path import basename

period = 5

def elapsed_time(start, end):
    secs = int(round(end - start))
    return '{:02}:{:02}'.format(int(secs / 60), secs % 60)

def calc(cur, prev):
    return float(cur - prev) / period

if len(argv) < 2:
    print('usage: {} <log-file>'.format(basename(argv[0])))
    exit(1)

out = open(argv[1], 'w')
start = time()

last = None
last_status = ''

try:
    while True:
        net = psutil.net_io_counters(True)['lo0']

        # ts=1404974147, bytes_sent=2066180, bytes_recv=2066180, packets_sent=24336, packets_recv=24336, errin=0, errout=0, dropin=0, dropout=0
        o = 'ts={}'.format(int(round(time())))
        for (k,v) in vars(net).items():
            o += ', {}={}'.format(k, v)
        out.write(o + '\n')

        # 00:15 --> in = 789B | 89P ; out = 126B | 7P
        s = elapsed_time(start, time())
        if last is not None:
            s += ' --> {:.2f}B/s | {:.2f}P/s'.format(
                    # loopback: sent==recv
                    calc(net.bytes_recv * 2, last.bytes_recv * 2),
                    calc(net.packets_recv * 2, last.packets_recv * 2),
                )
        s += ' ' * (len(last_status) - len(s))
        print(s, end='', flush=True)
        print('' * len(s), end='')

        last = net
        last_status = s
        sleep(period)

except KeyboardInterrupt:
    pass

end = time()
out.close()

print('\ntotal time: {}'.format( elapsed_time(start, end)))

