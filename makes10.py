"""
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.


makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True
"""

def makes10(a, b):
  if a+b ==10:
    return True
  if a==10 or b==10:
    return True
  else:
    return False
