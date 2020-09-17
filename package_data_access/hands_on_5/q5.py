import os
import json

def func1(value):
    # a= json.dumps(value)
    b= json.loads(value)
    return b

if __name__ == "__main__":
    try:
        data=input()
        b=func1(data)
        print(True)
        print(b[1].values())
    except ValueError as error:
        print(False)
