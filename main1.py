"""from math_toolkit.operations import add, subtract, multiply, divide

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(add(a,b))
print(subtract(a, b))
print(multiply(a,b))
print(divide(a, b))"""

import roulette

# Initialize the roulette wheel
wheel = roulette.Wheel()

# Spin the wheel
result = wheel.spin()

# Print the result of the spin (number and color)
print("Spin result:", result)

# Example of placing a bet on a color (red or black)
bet = roulette.Bet(10, "red")  # Bet 10 units on red
print("Placed bet:", bet)

# Check if the bet was won
if bet.check(result):
    print("You won!")
else:
    print("You lost!")
