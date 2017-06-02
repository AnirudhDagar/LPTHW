#Appending a file means that you are adding or essentialy
from sys import argv
script, filename = argv

print "Now we'll try to append a file and see what happens"
target=open(filename,'a')
print "Now write the line."
line4=input("line 4:")
target.write(line4)
target.write("\n")
target.close()
input("Press q to quit > ")#I have added just to make the window stay and not quit.But it is useless :P 