"""
Given a string, return a new string where the first and last chars have been exchanged.


front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
"""

def front_back(s):
    if len(s) <= 1:
        return s
    return s[-1] + s[1:-1] + s[0]