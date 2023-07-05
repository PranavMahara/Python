#'0' is true actually
dict4 = {'0':False}
#all false
dict5 = {0:False}
print('All True Keys::',any(dict1))
print('One False Key ::',any(dict2))
print('Empty Dictionary ::',any(dict3))
print('With 0 in single quotes ::',any(dict4))
print('all false :: ',any(dict5))



# d3= {**d1, **d2} Join two dictionaries.