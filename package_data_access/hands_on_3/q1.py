import os
import re


# Enter your code here
def function(a):
    match = re.match(r'^[AEIOU].*?[aeiou]$', a)

    return match


if __name__ == "__main__":
    a = input()
    b = function(a)

    if b:
        print(True)

    else:
        print(False)