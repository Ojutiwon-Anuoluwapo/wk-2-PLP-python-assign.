my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert(1, 15)

print(my_list)  # Output: [10, 15, 20, 30, 40]

my_list2 = [50, 60, 70]
my_list.extend(my_list2)

print(my_list)  # Output: [10, 15, 20, 30, 40, 50, 60, 70]

del my_list[-1]  # Remove the last element
print(my_list)  # Output: [10, 15, 20, 30, 40, 50, 60]

my_list.sort()  # Sort the list
print(my_list)  # Output: [10, 15, 20, 30, 40, 50, 60]

print(my_list[3])