# Enter your code here.
import os
import pickle
class Player:
    def __init__(self, name, runs):
        self.name = name
        self.runs = runs
    
    
#Write code here to access value for name and runs from class PLayer    
myPlayer=  Player('dhoni', 10000)
    
#Write code here to store the object in pickle file
with open('test.pickle', 'wb') as outfile:
    pickle.dump(myPlayer, outfile)

del myPlayer

#Write code here to read the pickle file 
with open('test.pickle', 'rb') as outfile:
    myPlayer = pickle.load(outfile)

