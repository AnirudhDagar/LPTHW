formatter="%r %r %r %r"
#I learnt that r and s have a diffrence because r just prints what is written on the screen as it is.
#it is know as representation or raw format 
#do change r to s and re run the program

print (formatter % (1,2,3,4))
print (formatter % ("one","two","three","four"))
print (formatter % (True,False,True,False))
print (formatter % (formatter,formatter,formatter,formatter))
print (formatter % ("I wrote","this string","just to show","how i have learnt formatting"))
