#!/usr/bin/env python
# -*- coding: utf8 -*-

# author: xiaofengfeng
# create: 2016-12-05 17:15:56

import random


def miller_rabin_primality_testing(n, k):
    """
    Miller–Rabin primality test:"https://en.wikipedia.org/wiki/Miller–Rabin primality test"
    """
    if n < 10:
        return n in (2, 3, 5, 7)
    d = n - 1
    r = 0
    while not (d & 1):
        r += 1
        d >>= 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                break
        else:
            return False
    return True
