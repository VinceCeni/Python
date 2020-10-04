from abc import ABC, abstractmethod
class vehicle(ABC):
    def paySlip(self, amount):
        print("Your purchase amount: ",amount)
    @abstractmethod
    def payment(self, amount):
        pass

class DebitPayment(vehicle):
    def payment(self, amount):
        print('Your purchase of {} exceeded your $1000 limit '.format(amount))

obj = DebitPayment()
obj.paySlip("$4000")
obj.payment("$4000")

