num = int(input("Enter a number: "))

#check both numbers if divisible by 3 and 5
if num % 3 == 0 and num % 5 == 0:
    print("Bigyan ng jacket!")
#check if number is divisible by 3
elif num % 3 == 0:
    print("Hep! Hep!")
#check if number is divisible by 5
elif num % 5 == 0:
    print("Horaaay!")
#display if numbers is not divisible by 3 or 5 
else :
    print(f"{num} Tawsan!")
