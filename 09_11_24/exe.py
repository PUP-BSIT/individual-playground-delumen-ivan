
name = {'John': 80, 'Alice': 92, 'Bob': 85, 'Charlie': 92}
max_keys = [key for key, value in name.items() if value == max(name.values())]

print(max_keys)
