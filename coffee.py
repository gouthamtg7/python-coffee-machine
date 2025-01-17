print("Welcome to COFFEE MACHINE")
r = bool()
water = 300
milk = 200
coffee = 100
machine_off = False
money = 0
transactions = list()
penny = 0
dime = 0
nickel = 0
quarter = 0
price = 0
payment = bool
def menu():
    print("Expresso - 1.5$\nLatte - 2.5$\nCappucino - 3$\n* Kindly type your order without typos...Thank you *\n")
def make_expresso(water,coffee):
        water -= 50
        coffee -=18
def make_latte(water, coffee,milk):
        water -= 200
        coffee -=24
        milk -= 150
def make_cappucino(water, coffee,milk):
        water -= 250
        coffee -=24
        milk -=100
def report(water,milk,coffee,money):
    print("REPORT :")
    print(f"Water : {water}")
    print(f"Milk : {milk}")
    print(f"Coffee: {coffee}")
    print(f"Money Collected : {money}")

def refund(r):
    if r==True:
        print(f"Your {transactions[-1]}$ successful")

def order_availabiltiy(water,milk,coffee):
    if order == "expresso":
        if coffee < 24:
            print("Sorry item not available.\nRefund initiated...")
            r = True
        elif milk < 150:
            print("Sorry item not available.\nRefund initiated...")
            r = True
        elif water < 200:
            print("Sorry item not available.\nRefund initiated...")
            r = True
        else :
            r = False
def check_transactions(penny,dime,nickel,quarter):
    global payment
    global price
    if order =="expresso":
        price = 1.5
    elif order =="latte":
        price = 2.5
    elif order == "cappucino":
        price = 3
    if ((penny+dime+nickel+quarter) - price )<0:
        print(f"Sorry payment unsuccessful.\nYour short by {(price - (penny+dime+nickel+quarter))}$")
        payment = False
    elif((penny+dime+nickel+quarter) - price)>0:
        print(f"Payment successful.\nKindly collect your change of {(penny+dime+nickel+quarter) - price}$.\nYour order is being processed.")
        payment = True
        transactions.append(price)
    elif ((penny+dime+nickel+quarter) - price)==0:
        print(f"Payment successful.\nYour order is being processed...")
        payment = True
        transactions.append(price)




menu()
while machine_off == False:
    order = input("What would you like to have ??\nType 'menu' for menu.\n").lower()
    if order == "report":
        report(water,milk,coffee,money)
    elif order == "off":
        machine_off=True
    elif order=="menu":
        menu()
        continue
    #Check it's availability
    #Check the transactions
    #Then proceed
    order_availabiltiy(water,milk,coffee)
    if r==False:
        # Check the transactions
        print("Please insert the coins...")
        penny = int(input("Enter number of pennies:\n"))*0.01
        dime = int(input("Enter number of dimes:\n"))*0.1
        nickel = int(input("Enter number of nickels:\n"))*0.05
        quarter = int(input("Enter number of quarters:\n"))*0.25
        check_transactions(penny,dime,nickel,quarter)
        if payment==True:
            if order == "expresso":
                make_expresso(water, coffee)
            elif order == "latte":
                make_latte(water, coffee, milk)
            elif order == "cappucino":
                make_cappucino(water, coffee, milk)
            print(f"Here's your {order} ☕\nHave a great day 😇")
    refund(r)





















