# An exception is an event that cocurs during the execution of programs that disrupt the normal flow of execution
# 2 types of error
# 1) Syntax Error
# 2) Logical Error

# When an exception occurs, Python stops the program execution and generates an exception message. It is
# highly recommended to handle exceptions. The doubtful code that may raise an exception is called risky code.
# To handle exceptions we need to use try and except block. Define risky code that can raise an exception inside
# the try block and corresponding handling code inside the except block
'''
try:
    a = 10
    b = 0
    c = a/b
    print("The answer of a divide by b is ", c)

except:
    print("Error dude....zero")

'''

# It is good practice to specify an exact exception that the except clause should catch. For example, to catch an
# exception that occurs when the user enters a non-numerical value instead of a number, we can catch only the
# built-in ValueError exception that will handle such an event properly.
# We can specify which exception except block should catch or handle. A try block can be followed by multiple
# numbers of except blocks to handle the different exceptions. But only one exception will be executed when an
# exception occurs.
'''
try:
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    c = a/b
    print("The answer of a divide by b:", c)
except ValueError:
    print("Entered value is wrong")
except ZeroDivisionError:
    print("Can't divide by zero")
'''
# except(ValueError, ZeroDivisionError):
#   print("Please enter a valid value")

# Sometimes we want to execute some action at any cost, even if an error occurred in a program. In Python, we
# can perform such actions using a finally statement with a try and except statement.
# The block of code written in the finally block will always execute even there is an exception in the try and
# except block.
# If an exception is not handled by except clause, then finally block executes first, then the exception is thrown.
# This process is known as clean-up action.


try:
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    c = a / b
    print("The answer of a divide by b:", c)
except ZeroDivisionError:
    print("Can't divide with zero")

finally:
    print("Inside a finally block")


# try: The try block for risky code that can throw an exception.
# except: The except block to handle error raised in a try block.
# else: The else block is executed if there is no exception.

'''
try:
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    c = a / b
    print("a/b = %d" % c)
except ZeroDivisionError:
    print("Can't divide by zero")
else:
    print("We are in else block ")
'''

# The raise statement is useful in situations where we need to raise an exception to the caller program. We can
# raise exceptions in cases such as wrong data received or any validation failure.

'''
def simple_interest(amount, year, rate):
    try:
        if rate > 100:
            raise ValueError(rate)

        interest = (amount * year * rate) / 100
        print('The Simple Interest is', interest)
        return interest
        
    except ValueError:
        print('interest rate is out of range', rate)


print('Case 1')
simple_interest(800, 6, 8)
print('Case 2')
simple_interest(800, 6, 800)
'''


'''
try:
    age = -10
    print("Age is:")
    print(age)
    if age < 0:
        raise ValueError
    yearOfBirth = 2021-age
    print("Year of Birth is:")
    print(yearOfBirth)

except ValueError:
    print("Input Correct age.")
'''
# To create a user defined exception, we create a class with desired exception name which should inherit 
# Exception class. After that, we can raise the exception in our code anywhere according to our need to 
# implement constraints.
# To generate a user defined exception, we use the “raise” keyword when a certain condition is met. The 
# exception is then handled by the except block of the code. We then use pass statement. pass statement is used to 
# show that we will not implement anything in our custom exception class. It is used as a placeholder and does 
# nothing, still we have to use it because if we leave the body of our custom class empty, python interpreter will 
# show that there is error in our code.
