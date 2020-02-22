#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    percent = meal_cost / 100
    tip = percent * tip_percent
    tax = percent * tax_percent
    print round(meal_cost + tip + tax)


if __name__ == '__main__':
    meal_cost = float(raw_input())

    tip_percent = int(raw_input())

    tax_percent = int(raw_input())

    solve(meal_cost, tip_percent, tax_percent)
