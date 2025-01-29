def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    If the discount is 20% or higher, it is applied; otherwise, the original price is returned.
    
    :param price: float - The original price of the item
    :param discount_percent: float - The discount percentage
    :return: float - The final price after discount
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price

# Prompting user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate final price
    final_price = calculate_discount(price, discount_percent)

    # Display result
    print(f"The final price after discount is: ${final_price:.2f}")
except ValueError:
    print("Invalid input! Please enter numeric values.")
