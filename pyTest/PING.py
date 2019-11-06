# encoding: utf-

import time
import struct
import socket
import select
import sys


def checksum(data):
    n = len(data)
    m = n % 2
    sum = 0
    for i in range(0, n-m, 2):
        sum += (data[i]) + ((data[i+1]) << 8)
    if m:
        sum += (data[-1])
    sum = (sum >> 16) + (sum & 0xffff)
    sum += (sum >> 16)
    answer = ~sum & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer

if __name__ == '__main__':
    i = input()
    ping(i)