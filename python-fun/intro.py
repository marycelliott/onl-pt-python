# ======================================== #
# BASICS
# ======================================== #

# Declare a variable
my_list = [1,2,3,4] # this is a list, not an array
{"name": "Claire"} # this is a dictionary, not an object
# Show text on the console 
print("hello!") # python 3

# Get the length of something 
len(my_list)

# Add an item to a list
my_list.append(5)

# Remove last item
my_list.pop()

# Remove specific item from a list
my_list.pop(2)

# ======================================== #
# LOOPS
# ======================================== #

# For loop with numbers 
for num in range(0,7,1):      
    print(num) # 0 - 6

# For-in loops
my_list = [1,2,3,4]
for i in my_list:
    print(i) # value at index position

my_dict = {"name": "Claire", "age": 30, "pets": [], "has_siblings": True}
for k in my_dict:
    print(k) # print the keys
    print(my_dict[k]) # print value of that key


# ======================================== #
# CONDITIONAL STATEMENTS
# ======================================== #
# if condition1 or condition2:
#     pass
# elif condition1 and condition2:
#     pass
# else:
#     pass


# ======================================== #
# FUNCTIONS
# ======================================== #

# Declare a function 
def function_name(param1,param2):
    for i in range(6):
        print(i)

# Call a function
# function_name(argument1, argument2)

