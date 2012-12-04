my_name = 'Jordan'
my_age = 25 # My age 
my_height = 71 # inches
my_weight = 165 # lbs
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'
my_race = 'Black'
# Add pauses to code 
print "Let's talk about %s." % my_name
raw_input()
print "He is and %s Man." % my_race
raw_input()
print "He's %d inches tall." % my_height
raw_input()
print "He's %d pounds heavy." % my_weight
raw_input()
print "Actually that's not too heavy."
raw_input()
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
raw_input()
print "His teeth are usually %s depending on the his smoking habit." % my_teeth
raw_input()
# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
