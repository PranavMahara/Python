word = "Hello World"
print(word.isalnum())    #check if all char are numbers
print(word.isalpha())    #check if all char in the string are alphabetic
print(word.isdigit())    #test if string contains digits

# Format strings contains curly braces {} as placeholders or replacement fields which gets replaced. 
# We can use positional arguments or keyword arguments to specify the order.

# default(implicit) order
# "{}, {} and {}".format(‘aaa’,‘bbb’,‘ccc')  
# ‘aaa,bbb,ccc‘

print("{}, {} and {}".format('aaa', 'bbb', 'ccc'))

# order using positional argument
#  "{1}, {0} and {2}".format(' aaa’,‘bbb’,‘ccc') 
# ‘bbb, aaa and ccc'

print("{1}, {0} and {2}".format('aaa', 'bbb', 'ccc'))

# order using keyword argument
# "{c}, {b} and {a}".format(a=‘aaa',b=‘bbb',c=‘ccc')
# ‘ccc,bbb and aaa‘

print("{c}, {b} and {a}".format(a='aaa', b='bbb', c='ccc'))
