# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


user_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

for i in range(len(user_list)):
    for j in range(i+1, len(user_list)):
        if user_list[i][-1] >= user_list[j][-1]:
            user_list[i],user_list[j]= user_list[j],user_list[i]

print("List number form list is :",user_list)    



#### Thank You....















