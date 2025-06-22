from collections import UserList


class AmountPaymentList(UserList):
    def amount_payment(self):
        sum = 0
        for value in self.data:
            if value > 0:
                sum = sum + value
        return sum
    
payment = [1, -3, 4]
apl = AmountPaymentList(payment)
print(apl.amount_payment())