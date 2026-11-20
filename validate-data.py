#!/usr/bin/env python3
import sys

MAX_NAME = 15
MAX_MOBILE = 10

if len(sys.argv) != 3:
    print("FAIL")
    sys.exit(1)

name, mobile = sys.argv[1], sys.argv[2]

if len(name) <= MAX_NAME and len(mobile) <= MAX_MOBILE:
    print("PASS")
else:
    print("FAIL")
