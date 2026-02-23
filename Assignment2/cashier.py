class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        try:
            large_dollars = int(input("How many large dollars?: "))
            half_dollars = int(input("How many half dollars?: "))
            quarters = int(input("How many quarters?: "))
            nickels = int(input("How many nickels?: "))
        except ValueError:
            print("That's not a number. Start again.")
            return 0

        total = (large_dollars * 1.00) + (half_dollars * 0.50) + (quarters * 0.25) + (nickels * 0.05)
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient."""
        if coins >= cost:
            change = round(coins - cost, 2)
            print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry there is not enough money. Money Refunded.")
            return False