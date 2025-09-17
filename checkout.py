from payment_modes import PaymentMode
from handlers import (
    handle_paypal,
    handle_googlepay,
    handle_creditcard,
    handle_unknown
)

# Dispatch dictionary
payment_dispatch = {
    PaymentMode.PAYPAL: handle_paypal,
    PaymentMode.GOOGLEPAY: handle_googlepay,
    PaymentMode.CREDITCARD: handle_creditcard,
    PaymentMode.UNKNOWN: handle_unknown
}

def checkout(mode: PaymentMode, amount: float):
    handler = payment_dispatch.get(mode, handle_unknown)
    handler(amount)
