import shutil
import os
from  hashlib import md5
if __name__ == '__main__':
    # source = os.path.join(os.getcwd(), 'New Dir/')
    # destination = os.getcwd()
    # for file in os.listdir(source):
    #     shutil.copy(source+file, destination)
    #
    #
    # print(source)
    # print(destination)
    print(md5(str.encode('/projects/challenge/newww.txt')).hexdigest())