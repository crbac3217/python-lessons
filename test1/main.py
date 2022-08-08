from coffee import MENU, resources


curResource = resources
curMoney = 0
#Initial Statement
def printInitial():
    inputStatement = input("what do you want (espresso, americano, cappucino)? ")
    if(inputStatement == "report"):
        processReport()
    else:
        processCoffee(inputStatement)

#print report
def processReport():
    print(curResource)
    print(curMoney)

#processCoffee
def processCoffee(coffeeName):
    selCoffee = {}
    for coffee in MENU:
        if coffee == coffeeName:
            print("coffee exists")
            selCoffee = coffee
            return
    print("Checking if we got enough resources")


printInitial();