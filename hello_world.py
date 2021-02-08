# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Brandon"
print("Hello", name)	# with a comma
print("Hello " + name)	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello", name)	# with a comma
print("Hello " + str(name))	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}") # with an f string

# Playing with strings

first_name = "firstName"
last_name = "lastName"
full_name = "Brandon Hansen"

class returnValue:
    def __init__(self, r1, r2):
        self.r1 = r1
        self.r2 = r2

def getSplitName(full_name):
    split_location = full_name.split(" ")
    first_name = split_location[0]
    last_name = split_location[1]
    return returnValue(first_name, last_name)

first_name = getSplitName(full_name).r1
last_name = getSplitName(full_name).r2
print(f"first_name = {first_name} | last_name = {last_name}")
