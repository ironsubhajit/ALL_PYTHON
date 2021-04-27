# need a algorithm


from datetime import datetime


class Products:
    pass


def check_product_price():
    pass


def select_product():
    # checking for each product price
    products = Products()
    print("Product Items List:\n===============\n")
    for item in products.items():
        print(f"{item}\n")
    product_id = input("Enter Product id: ")
    product_price_for_each = check_product_price(product_id)

    # calculate buying cost
    product_unit = get_product_price_unit(product_name)  # in which Product-Quantity is measured
    product_quantity = int(input(f"Enter {product_name}'s Quantity: "))
    total = calculate_product_cost(product_price_for_each, product_quantity, product_unit)
    return total




print("billing System online...")
quit = False
current_date = datetime.now().date()
customer_name = "john" #input("Enter Customer name: ")
customer_ph_no = "123" #input("Enter Customer phone number: ")

total_price_to_pay = 0
# quit == False
while not quit:
    total_price_to_pay += select_product()
    print(f"Total: INR {total_price_to_pay}")




bill_no = 0
bill_receipt = f"""
                Super Bazaar Bill Receipt
    Phone No: 123456789, Amrity, Malda, Pin: 732207

==============================================================
Bill No:       {bill_no}        Date: {current_date}
Customer Name: {customer_name}  Phone Number: {customer_ph_no}
==============================================================
Product         | Quantity          | Price (INR)   |
==============================================================
{product_name}  | {product_quantity}|{product_price}|
"""
print(bill_receipt)