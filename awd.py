"""fruits = ["Strawberries", "Spinach", "Kale"]
vegetables = ["Tomatoes", "Celery", "Potatoes"]
food = [fruits, vegetables]
print(food[0][2])


for number in range(5, 10, 2):
    print(number)"""

'''message = "Starting Loop"
while message != "exit":
    print(message)
    message = input("Enter your message: ")

print("Loop Ended")'''

'''for num in range(5) :
    if num % 2 != 0 :
        print("_")
        continue
    print(num)'''

'''message = "Hello World!"
def greet():
    message = "Hi There!"
    print(message)

greet()
print(message)'''

'''message = "Hello World!"
def greet():
    global message
    message = "Hi There!"
    print(message)

greet()
print(message)'''

def get_message():
    return "Hello World"

print(get_message)

