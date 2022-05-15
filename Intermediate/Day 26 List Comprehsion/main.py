# Consider the list
numbers = [1, 2, 3]

# # We can add 1 to every member of the list
#
# new_list = []
#
# for num in numbers:
#     add_1 = num + 1
#     new_list.append(add_1)
# print(new_list)

# List comprehension makes it easier

#  new_list = ['what to do with item' for 'item' in 'original list']

new_list = [num + 1 for num in numbers]
print(new_list)

# You can use it for sequences

# We can add condition!

#  new_list = ['what to do with item' for 'item' in 'original list' if 'condition is met']

# Dictionary comprehension
# new_dict = {new_key: new_value for (key, value) in list if 'condition is met' }

# new_dict = {new_key: new_value for (key, value) in dict.items if 'condition is met' }

# how to use loops with pandas
# for (index, row) in dataframe.iterrows():
#   print(row.column_name)