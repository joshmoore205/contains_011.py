#!/usr/bin/env python3

import sys

def contains(left, right):
  for c in left:
    if c not in right:
      return False
    right = right.replace(c, "", 1)
  return True


for line in sys.stdin:
  left, right = line.strip().lower().split()
  print(contains(left, right))
