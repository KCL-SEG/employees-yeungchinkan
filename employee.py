"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, isContract, contractHour, pay, bonus, commission, contractNum):
        self.name = name
        self.isContract = isContract
        self.contractHour = contractHour
        self.pay = pay
        self.bonus = bonus
        self.commission = commission
        self.contractNum = contractNum

    def get_pay(self):
        if self.isContract:
            return self.pay * self.contractHour + self.bonus + self.commission * self.contractNum
        else:
            return self.pay + self.bonus + self.commission * self.contractNum

    def __str__(self):
        msg = self.name + " works on a "
        if self.isContract:
            msg += "contract of " + str(self.contractHour) + " hours at " + str(self.pay) + "/hour"
        else:
            msg += "monthly salary of " + str(self.pay)
        if self.bonus > 0:
            msg += " and receives a bonus commission of " + str(self.bonus) 
        elif self.commission > 0:
            msg += " and receives a commission for " + str(self.contractNum) + " contract(s) at " + str(self.commission) + "/contract"
        msg += ". Their total pay is " + str(self.get_pay())
        return msg


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', False, 0, 4000, 0, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', True, 100, 25, 0, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', False, 0, 3000, 0, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', True, 150, 25, 0, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', True, 0, 2000, 1500, 0, 0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', True, 120, 30, 600, 0, 0)
