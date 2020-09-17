import os
#Write your code here
s = os.getcwd()
os.mkdir('New Folder')
os.chdir('New Folder')
q = os.getcwd()
os.chdir('../')
os.rename('New Folder', 'New Folder2')
os.chdir('New Folder2')
p = os.getcwd()
os.chdir('../')
os.rmdir('New Folder2')
w = os.getcwd()











with open('.hidden.txt','w') as outfile:
     outfile.write(s)
with open('.hidden1.txt', 'w') as outfile:
     outfile.write(q)
with open('.hidden2.txt', 'w') as outfile:
     outfile.write(p)
with open('.hidden3.txt', 'w') as outfile:
     outfile.write(w)


