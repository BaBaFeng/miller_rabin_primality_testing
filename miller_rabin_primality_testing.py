#!/usr/bin/env python
# -*- coding: utf8 -*-

# author: xiaofengfeng
# create: 2016-12-05 17:15:56


def num_bits(num):
    return len(bin(num)) - 2


def miller_rabin_primality_testing(n):
    a = 7
    for _ in range(0, 7):
        x = pow(a, 7, n)
        if x == 1 or x == n - 1:
            print(True)


if __name__ == '__main__':
    miller_rabin_primality_testing(97)
