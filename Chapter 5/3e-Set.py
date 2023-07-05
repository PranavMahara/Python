# In addition to the difference(), there is one more method called difference_update(). 
# There are two main differences between these two methods.
# • The difference() method will not update the original set 
# while difference_update() will update the original set.
# • The difference() method will return a new set with only the unique elements 
# from the set on which this method was called. difference_update() will not 
# return anything

color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
remaining_colors = {'indigo', 'orange', 'red'}
# difference of two sets
new_set = color_set.difference(remaining_colors)
print(new_set)
# output {'violet', 'yellow', 'green', 'blue'}
# original set after difference
print(color_set)
# {'green', 'indigo', 'yellow', 'blue', 'violet'}
# difference of two sets
color_set.difference_update(remaining_colors)
# original set after difference_update
print(color_set)
# Output {'green', 'yellow', 'blue', 'violet'}


# In addition to the symmetric_difference(), there is one more method 
# called symmetric_difference_update(). There are two main differences between these two 
# methods.
# The symmetric_difference() method will not update the original set 
# while symmetric_difference_update() will update the original set with the unique elements 
# from both sets.

color_set = {'violet', 'indigo', 'blue', 'green', 'yellow'}
remaining_colors = {'indigo', 'orange', 'red'}
# symmetric difference
unique_items = color_set.symmetric_difference(remaining_colors)
print(unique_items)
# output {'yellow', 'green', 'violet', 'red', 'blue', 'orange'}
# original set after symmetric difference
print(color_set)
# {'yellow', 'green', 'indigo', 'blue', 'violet'}
# using symmetric_difference_update()
color_set.symmetric_difference_update(remaining_colors)
# original set after symmetric_difference_update()
print(color_set)
# {'yellow', 'green', 'red', 'blue', 'orange', 'violet'}