import os
import re

# Enter your code here
sample_text = ['199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245',
               'unicomp6.unicomp.net - - [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985',
               '199.120.110.21 - - [01/Jul/1995:00:00:09 -0400] "GET /shuttle/missions/sts-73/mission-sts-73.html HTTP/1.0" 200 4085',
               'burger.letters.com - - [01/Jul/1995:00:00:11 -0400] "GET /shuttle/countdown/liftoff.html HTTP/1.0" 304 0',
               '199.120.110.21 - - [01/Jul/1995:00:00:11 -0400] "GET /shuttle/missions/sts-73/sts-73-patch-small.gif HTTP/1.0" 200 4179',
               'burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 304 0',
               'burger.letters.com - - [01/Jul/1995:00:00:12 -0400] "GET /shuttle/countdown/video/livevideo.gif HTTP/1.0" 200 0',
               '205.212.115.106 - - [01/Jul/1995:00:00:12 -0400] "GET /shuttle/countdown/countdown.html HTTP/1.0" 200 3985',
               'd104.aa.net - - [01/Jul/1995:00:00:13 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985',
               '129.94.144.152 - - [01/Jul/1995:00:00:13 -0400] "GET / HTTP/1.0" 200 7074',
               'unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /shuttle/countdown/count.gif HTTP/1.0" 200 40310',
               'unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 200 786',
               'unicomp6.unicomp.net - - [01/Jul/1995:00:00:14 -0400] "GET /images/KSC-logosmall.gif HTTP/1.0" 200 1204',
               'd104.aa.net - - [01/Jul/1995:00:00:15 -0400] "GET /shuttle/countdown/count.gif HTTP/1.0" 200 40310',
               'd104.aa.net - - [01/Jul/1995:00:00:15 -0400] "GET /images/NASA-logosmall.gif HTTP/1.0" 200 786']

mlist = []
for line in sample_text:
    m = re.search(r'(.*?)\s-\s-\s\[(.*?)]\s"([A-Z]+)\s(\/.*?)\s(.*?)"\s(\d+)\s(\d+)', line)
    mlist.append(m.groups())
def func1():
    hosts = []
    for line in mlist:
        hosts.append(line[0])
    print(hosts)


def func2():
    timestamps =[]
    for line in mlist:
        timestamps.append(line[1])
    print(timestamps)


def func3():
    method_uri_protocol = []
    for line in mlist:
        method_uri_protocol.append((line[2],line[3],line[4]))
    print(method_uri_protocol)


def func4():
    status =[]
    for line in mlist:
        status.append(line[5])
    print(status)


def func5():
    content_size = []
    for line in mlist:
        content_size.append(line[-1])
    print(content_size)


'''For testing the code, no input is to be provided'''

if __name__ == "__main__":
    func1()
    func2()
    func3()
    func4()
    func5()