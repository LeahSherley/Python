my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)
my_list.insert(2,15)

print(my_list)

another_list = [50,60,70]

my_list.extend(another_list)
print(my_list)

my_list.remove(70)
print(my_list)
#can also use pop method to use the index to remove the element
#can also use del my_list[1] and uses index to remove element


my_list.sort()
print(my_list)
#use sort(reverse=true) for descending order

value30 = my_list[3]
print(value30)

#or do this if index is unknown

my_list = [10, 20, 30, 40]
value = 30
for index, element in enumerate(my_list):
    if element == value:
        print(value)
        break


