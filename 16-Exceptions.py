#!/bin/python3

import sys


S = input().strip()
try:
    k = int(S)
    print(S)
except BaseException as error:
    print("Bad String")