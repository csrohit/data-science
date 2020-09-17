import os
import json


def func1(value):
    a = json.loads(value)
    datas = [item for item in a['data']]

    return datas


if __name__ == "__main__":
    try:
        data = input()
        b = func1(data)
        print(True)
        print(b)
    except ValueError as error:
        print(False)
