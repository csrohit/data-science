import os
import re


# Enter your code here
def function(a):
    result = re.match(r'^[A-Z].+', a)

    return result


if __name__ == "__main__":
    a = input()
    b = function(a)

    if b:
        print(True)

    else:
        print(False)