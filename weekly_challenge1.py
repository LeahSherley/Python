numbers = input("Enter a list of integers: ").split()
numbers = [int(num) for num in numbers]

total = sum(numbers)

print("The sum of the numbers is:", total)
books = ("One Day", "The Perfect Find", "The Summer I turned Pretty", "Fault in our Stars", "After")

for book in books:
   print(book)

information = {}
information['name'] = input("Enter your name:")
information['age']= input("Enter your age:")
information['color'] = input("Enter your favorit color:")

for key, val in information.items():
    print(f"{key}:{val}")

set1_input = input("Enter integers for the first set separated by spaces: ")
set1 = set(map(int, set1_input.split()))

   
set2_input = input("Enter integers for the second set separated by spaces: ")
set2 = set(map(int, set2_input.split()))
set_3 = set1.intersection(set2)

print("Both sets include:", set_3)

word_list = ["apple", "banana", "orange", "grape", "kiwi", "strawberry", "blueberry"]
odd_words = [word for word in word_list if len(word) % 2 != 0]

   
print("Words with odd number of characters:", odd_words)






