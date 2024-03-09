# My_list
num1 = []
print ("Before append:", num1)

# Appending elements
num1.append(10)
num1.append(20)
num1.append(30)
num1.append(40)
print ("After append:", num1)

# Additional value (15) insertion
num1.insert(1, 15)
print("list with 15:", num1)

# Extension of the original list
num2 = [50, 60, 70]
num1.extend(num2)
print("Extended list:", num1)

# Removal of the last element from the list
num1.remove(70)
print("amended list with the last element removed:", num1)

# Ascending order sorting
num1.sort()
print(num1)

# Printing the index of value 30
print(num1[3])
