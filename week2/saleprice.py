price: 0
raw_total: 0
discount: 0
total_discount: 0
sales_tax: 0
final_total: 0


product_descr = (input("Please enter your product description here: "))
product_quantity = int(input("How many of the " + product_descr + " would you like to purchase? "))
product_price = float(input("What is the price of the item? " ))
raw_total = product_price * product_quantity

if product_price > 39.99:
    discount = product_price * .25
   # product_price = (float(product_price - product_price * .25))
elif product_price > 19.99:
    discount = product_price * .15
   # product_price = (float(product_price - product_price * .15))
total_discount = discount * product_quantity
price = raw_total - total_discount


sales_tax = price * 0.065  
final_total = price + sales_tax
def formatting (amount):
    return "$" + str("{:,.2f}".format(amount)) 
print("Your Receipt"),
print("---------------------------------"),
print(product_descr, formatting(product_price) + " each"),
print("Sales Tax " + formatting(sales_tax)),
print("Total Amount Due " + formatting(final_total)),
print("You saved " + formatting(total_discount))
print("Thank you for shopping with us today!")  