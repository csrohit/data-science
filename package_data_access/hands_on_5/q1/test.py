from hashlib import md5
import prog
f = open(".hidden.txt", "r")
s=f.readline()
s=md5(str.encode(s)).hexdigest()
def test_s():
    assert s == "9369f2b9904049e1fc1bc1e5750fe86d"




