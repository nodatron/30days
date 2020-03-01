#!/bin/python

import math
import os
import random
import re
import sys


def printl(n, i, product):
    print "{} x {} = {}".format(n, i, product)

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(1, 11):
        printl(n, i, n*i)
