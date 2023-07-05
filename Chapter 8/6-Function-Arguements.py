# 4 Types --> 
# 1) Required arguments
# 2) Keyword arguments
# 3) Default arguments
# 4) Variable-length arguments


# 1)
# Required arguments are the arguments passed to a function in correct positional 
# order. Here, the number of arguments in the function call should match exactly with 
# the function definition

def printme( str ):
    "This prints a passed string into this function"
    print(str)
# Now you can call printme function
printme()


# 2)
# Keyword arguments are related to the function calls. When you use keyword 
# arguments in a function call, the caller identifies the arguments by the parameter 
# name.
# This allows you to skip arguments or place them out of order because the Python 
# interpreter is able to use the keywords provided to match the values with parameters. 

def printme( str ):
    "This prints a passed string into this function"
    print(str)
# Now you can call printme function
printme( str = "My string")
# Note that the order of parameters does not matter.

def printinfo( name, age ):
    "This prints a passed info into this function"
    print("Name: ", name)
    print("Age ", age)
 
# Now you can call printinfo function
printinfo(age=50, name="miki" )

# 3)
# A default argument is an argument that assumes a default value if a value is not provided in the function call for that argument
def printinfo( name, age = 35 ):
    "This prints a passed info into this function"
    print("Name: ", name)
    print("Age ", age)

# Now you can call printinfo function
printinfo( age = 50, name = "miki" )
printinfo( name = "miki" )

# 4)
# You may need to process a function for more arguments than you specified while 
# defining the function. These arguments are called variable-length arguments and are 
# not named in the function definition, unlike required and default arguments.
# Syntax for a function with non-keyword variable arguments is this −

# def functionname([formal_args,] *var_args_tuple ):
#       "function_docstring"
#       function_suite
#       return [expression]

# An asterisk (*) is placed before the variable name that holds the values of all 
# nonkeyword variable arguments. This tuple remains empty if no additional arguments 
# are specified during the function call. Following is a simple example −

def printinfo( arg1, *vartuple ):
    "This prints a variable passed arguments"
    print("Output is: ")
    print(arg1)
    for var in vartuple:
        print(var)

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )