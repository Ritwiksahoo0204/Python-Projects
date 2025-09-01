class MoneyMachine:

    CURRENCY = "₹"

    COIN_VALUES = {
        "One Rupee": 1,
        "Two Rupees": 2,
        "Five Rupees": 5,
        "Ten Rupees": 10,
        "Twenty Rupees": 20
    }

    def __init__(self):
        self.profit = 0

    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_payment(self, inserted_amount, cost):
        """Processes payment with given amount."""
        if inserted_amount >= cost:
            change = round(inserted_amount - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            return True, change
        else:
            print(f"Sorry that's not enough money. {self.CURRENCY}{inserted_amount} refunded.")
            return False, inserted_amount
