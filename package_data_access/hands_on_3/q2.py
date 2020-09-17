import os
import re


def function(a):
    m = re.match(r'^e.*?\se.*', a)

    return m


if __name__ == "__main__":
    a = input()
    b = function(a)

    if b:
        print(True)

    else:
        print(False)