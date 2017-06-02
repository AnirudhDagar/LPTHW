from sys import argv
script, user_name = argv
prompt=">"
#We are making a variable here prompt so that we can change it to anything and use it directly in raw_input without changing it everywhere.
#For example try changing prompt to Ans. or a * or a # sign.
print ("Hi %s, I'm the %s script." %(user_name,script))
print ("I would like to ask some questions")

print ("Do you like me %s?" %user_name)
likes=input(prompt)

print ("What type of PC do you use?")
PC=input(prompt)

print ("Where do you live?")
lives=input(prompt)

print ("""
Alright so you said %r about liking me.
You live in %r . I dont where it is though.
And you have %r PC.""" %(likes,lives,PC) )