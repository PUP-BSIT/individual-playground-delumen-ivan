all_items = [] # global list

#function for product details -Simone Reyes
def order_take():
    global product_name, product_price, product_quantity
    product_name =  input("Product Name: ")
    product_price = int (input("Price: "))
    product_quantity = int (input("Quantity: "))
    total = product_price * product_quantity

    return [product_name, product_price, product_quantity, total]

#taking order from customer - Ivan Delumen
is_order_again = True 
while is_order_again: # loop that continues as long as the user wants to add orders
    all_items.append(order_take())
    user_prompt = input("Would you like add another order? y - YES / n - NO: ")
    is_order_again = user_prompt == 'y' #type casting of user_prompt input to boolean

total_amount = sum(item[3] for item in all_items)

#function for senior citizen details - Daniel Victorioso
def senior_citizen_details(total_amount, senior_id_no):
    total_amount = sum(item[3] for item in all_items)
    if senior_id_no.strip() == "":
        return total_amount
    
    discount = total_amount * 0.10
    total_amount -= discount
    return total_amount

#buyer details and senior citizen details - Gerald Mamasalanang
buyer_name = input("\nWhat is your name: ")
senior_id_no = input("Senior ID no. (leave blank if not a senior): ")

total_amount = senior_citizen_details(total_amount, senior_id_no)

#Grand total and all details - Michael Mosquito
print("\n")
for item in all_items:
    print(f"Items: {item[0]}, Price: {item[1]}, Quantity: {item[2]}, Total: {item[3]}")
print(f"\nCustomer Name: {buyer_name}")
print(f"Senior ID No.: ", end="")
if senior_id_no:
    print(senior_id_no)
else:
    print()
print(f"Grand Total: {total_amount}")