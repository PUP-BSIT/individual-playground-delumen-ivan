string = str(input("Enter series of string: ")).lower()

count = {}

for key in string :
    count[key] = count.get(key, 0) + 1

print(count)