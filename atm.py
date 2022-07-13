cash=120000
class Atm():
    def __init__(self, cardNumber, pinNumber, cash):
        self.pinNumber = pinNumber
        self.cardNumber = cardNumber
        self.cash = cash
    
    def cashWithdrawl(self, cashWithdrawl):
        if(cashWithdrawl <= cash):
            self.cash=self.cash-cashWithdrawl
        else:
            print('Not enought cash in account')
        self.BalanceEnquiry()
    def BalanceEnquiry(self):
        print("your current balance is ",self.cash)
#john = Atm("john",12,"male",{math 3.3})
cardNumber = int(input("what is your card number?"))
pinNumber = int(input("Hello! Please enter your pin number"))
balance = int(input("Welcome! how much cash would you like to withdraw? Your balance is"))
print("User card number is", cardNumber)
atmObject = Atm(cardNumber,pinNumber,cash)
print(atmObject.cash)
atmObject.BalanceEnquiry()
atmObject.cashWithdrawl(balance)
atmObject.BalanceEnquiry()
'''card1 = "cardNumber"
card2 = 12
card3 = 1.5
card4 = False
print(card1,card2,card3,card4)'''
#print(type(cardNumber))
