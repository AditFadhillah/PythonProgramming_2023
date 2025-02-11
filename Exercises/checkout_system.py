
def add_percentage(price, percentage=15):
    return price * (1 + percentage / 100)

def add_tip(price):
    while True:
        tip_input = input("How much tip would you like to give? ")
        if tip_input.isdigit() and int(tip_input) >= 0:
            tip = int(tip_input)
            return add_percentage(price, tip)

def calculate_order(order, item_prices):
    total_price = 0

    for item in order:
        item_code = item.strip()
        if item_code in item_prices:
            total_price = total_price + item_prices[item_code]
    return total_price

def main():
    menu = """
    1. Habbeer ($3.50)
    2. Wine ($4.00)
    3. Java Coffee ($2.50)
    4. Apple Juice ($6.00)
    5. Root Access Beer ($1.75)
    """

    item_prices = {
    "1": 3.50,
    "2": 4.00,
    "3": 2.50,
    "4": 6.00,
    "5": 1.75,
    }

    print(menu)
    user_input = input("Please write down your order: ")

    total_price = calculate_order(user_input, item_prices)
    total_price = add_percentage(total_price)
    total_price = add_tip(total_price)

    print(f"\nTotal price: ${total_price:.2f}")

if __name__ == "__main__":
    main()
