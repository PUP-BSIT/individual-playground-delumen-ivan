'''response = (200,
           {'Content-Type' : 'application/json'},
            '{"name" : "Alice"}')
status_code, headers, body = response
print(type(status_code),)'''

"""def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1, 2, 3, 4, 5))
print(add(7, 4, 3))
print(add(1, 3, 4, 5))"""

"""def calculate(**kwargs):
    print(kwargs)

calculate(num_1=3, num_2=5, operator="+")"""

"""def calculate(**kwargs):
    for key, value in kwargs.items():
        print(f"key={key}, value={value}")

calculate(num_1=3, num_2=5, operator="+")"""

"""even_numbers = (1, 3, 8)
print(even_numbers[1]) #access items in tuple
for item in even_numbers: #iterating items in tuple
    print(item)
"""

"""ccord = (5, 7)
y, x = ccord
print(ccord)"""

"""pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)"""

"""pages = 0
word_per_page = 0
print(f"pages: {pages}, word_per_page: {word_per_page}")
pages = int(input("Number of pages: "))
print(f"pages after input: {pages}")
word_per_page == int(input("Number of words per page: "))
print(f"word_per_page after input: {word_per_page}")
total_words = pages * word_per_page
print(total_words)"""

def calculate_average(numbers) :
    total = sum(numbers)
    average = total / len (numbers)
    return average

numbers = []
user_input = int(input("Enter a number: "))
while user_input.isnumeric() :
    numbers.append(int(user_input))
    user_input = input("Enter a number: ")

print("Average: ", calculate_average (numbers))