from hashlib import md5
f = open(".hidden.txt", "r")
g= open(".hidden1.txt","r")
p=open(".hidden2.txt","r")
s=f.readline()
s1=g.readline()
s2=p.readline()
s=md5(str.encode(s)).hexdigest()
s1=md5(str.encode(s1)).hexdigest()
s2=md5(str.encode(s2)).hexdigest()
def test_s():
    assert s == "3644a684f98ea8fe223c713b77189a77"

def test_s1():
    assert s1 == "e9e2aa8136260a22b0b09fdee43ccb8a"

def test_s2():
    assert s2 == "2226724cc9f64fc1140b95a0e513dc6f"


