import os
import re


# Enter your code here. Read input from STDIN. Print output to STDOUT
def main(x):
    names = re.findall(r'[A-Z][a-z]*', x)
    values = re.findall(r'\d+', x)
    dicts = {}
    for i in range(len(names)):
        dicts[names[i]] = values[i]

    return dicts
    '''For testing the code, no input is to be provided'''


if __name__ == "__main__":
    x = input()
    print(main(x))