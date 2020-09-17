from hashlib import md5
f = open(".hidden.txt", "r")
f1 = open(".hidden1.txt", "r")
f2 = open(".hidden2.txt", "r")
f3 = open(".hidden3.txt", "r")

s=f.readline()
s=md5(str.encode(s)).hexdigest()

w=f1.readline()
w=md5(str.encode(w)).hexdigest()

e=f2.readline()
e=md5(str.encode(e)).hexdigest()

x=f3.readline()
x=md5(str.encode(x)).hexdigest()

def test_s():
    assert s == "717314d1aa06c162e38fb37871f56aab"
def test_w():
    assert w == "3b53febc910ab0d559c140bc45c86995"
def test_e():
    assert e == "926780478d496bffc072b870ef54b301"
def test_x():
    assert x == "717314d1aa06c162e38fb37871f56aab"

