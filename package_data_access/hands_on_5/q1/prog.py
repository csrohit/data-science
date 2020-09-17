# Enter your code here. 
import pickle
import os
data={
    "a":[5,9],
    "b":[5,6],
    "c":["Pickle is","helpful"]
}
#Dump file in pickle
with open("test.pkl","wb") as outfile:
    pickle.dump(data,outfile)

del data
#Read data back from pickle
with open("test.pkl","rb") as outfile:
    data=pickle.load(outfile)
    
print(data)
pickles = []       
for root,dirs,files in os.walk("./"):
    # root is the dir we are currently in, f the filename that ends on ...
    pickles.extend( (os.path.join(root,f) for f in files if f.endswith(".pkl")) )
pickles=str(pickles)
print(pickles)

with open('.hidden.txt','w') as outfile:
	outfile.write(pickles)




