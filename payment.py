from abc import ABC, abstractmethod
import datetime


class PaymentGateway(ABC):

    @abstractmethod
    def charge(self, amount: float, currency: str) -> dict: ...

    @abstractmethod
    def refund(self, txn_id: str, amount: float) -> bool: ...

    def generate_receipt(self, amount, currency, txn_id):
        return {
            "txn_id": txn_id,
            "amount": amount,
            "currency": currency,
            "gateway": self.__class__.__name__,
            "time": datetime.datetime.now().isoformat(),
        }


class RazorpayGateway(PaymentGateway):
    def charge(self, amount, currency="INR"):
        txn = f"rzp_{id(self):x}"
        print(f"[Razorpay] Charging {currency} {amount}")
        return self.generate_receipt(amount, currency, txn)

    def refund(self, txn_id, amount):
        print(f"[Razorpay] Refunding {amount}")
        return True


class StripeGateway(PaymentGateway):
    def charge(self, amount, currency="USD"):
        txn = f"stripe_{id(self):x}"
        print(f"[Stripe] Charging {currency} {amount}")
        return self.generate_receipt(amount, currency, txn)

    def refund(self, txn_id, amount):
        print(f"[Stripe] Refunding {amount}")
        return True


def process_payment(gw: PaymentGateway, amount, currency):
    receipt = gw.charge(amount, currency)
    print("Receipt:", receipt)


process_payment(RazorpayGateway(), 999, "INR")
process_payment(StripeGateway(), 19.99, "USD")
