"""

Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.


near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False
"""
def near_hundred(n):
  return ((abs(100-n)<=10) or (abs(200-n)<=10))


"""
🧠 Explanation:
abs(100 - n) means: "How far is n from 100?"

<= 10 means: "Is that distance 10 or less?"

Same logic for 200.

So:

If n = 93:
abs(100 - 93) = 7 → ✅ less than 10 → returns True

If n = 89:
abs(100 - 89) = 11 → ❌ more than 10
abs(200 - 89) = 111 → ❌ more than 10 → returns False
"""