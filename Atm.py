class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("Your balance is 1000")

    def withdrawl(self,cash):
        new_cash = 1000 - cash
        print("you have withdrawn cash "+str(cash) +". Your remaining balance is "+ str(new_cash))

def atm():
    card_number = input("insert your card number: ")
    pin_number  = input("enter your pin number: ")
    person =  Atm(Card_number ,pin_number)
    print("choose your activity ")
    print("1.check balance   2.withdrawl cash")
    activity = int(input("enter activity number: "))

    if (activity == 1):
        person.check_balance()
    elif (activity == 2):
        cash = int(input("enter the amount:- "))
        person.withdrawl(cash)
    else:
        print("enter a valid number")


if __name__ == "__atm__":
    atm()