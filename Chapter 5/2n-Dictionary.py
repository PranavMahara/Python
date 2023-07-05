#dictionary with both 'true' keys
dict1 = {1:'True',1:'False'}
#dictionary with one false key
dict2 = {0:'True',1:'False'}
#empty dictionary
dict3= {}
#'0' is true actually
dict4 = {'0':False}
print('All True Keys::',all(dict1))
print('One False Key',all(dict2))
print('Empty Dictionary',all(dict3))
print('With 0 in single quotes',all(dict4))