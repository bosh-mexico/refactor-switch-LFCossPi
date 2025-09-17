def handle_paypal(amount: float):
    print(f"Processing PayPal payment of ${amount:.2f}")
    # PayPal-specific logic here

def handle_googlepay(amount: float):
    print(f"Processing GooglePay payment of ${amount:.2f}")
    # GooglePay-specific logic here

def handle_creditcard(amount: float):
    print(f"Processing Credit Card payment of ${amount:.2f}")
    # Credit Card-specific logic here

def handle_unknown(amount: float):
    print("Invalid payment mode selected!")
