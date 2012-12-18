tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm\\ a \\ cat."

fat_cat = """
I'll do a list: 
\t* Cat food
\t* Fishes
\t* Catnip \n\t* Grass
"""
print tabby_cat 
print persian_cat
print backslash_cat
print fat_cat 

test1 = " \tfeel \nLike \nDrinking " 
test2 = "So\\I\\will\nWhen I get home" 



print "How do you feel %s" % test1
print "What are you going to do? %r" % test2 

# Nice animation effect
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
