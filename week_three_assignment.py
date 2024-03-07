def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


final_price = calculate_discount(100, 25)
print("Final price after discount:", final_price)

def calculate_discount(price, discount_percent):
    price = float(price)
    discount_percent = float(discount_percent)
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


original_price = input("Enter original price")
discount_percentage = input("Enter Discount percentage:")
final_price = calculate_discount(original_price, discount_percentage)

if final_price != original_price:
    print(f"Final price after discount: ${final_price}")
else:
    print(f"Original price: ${original_price}")
