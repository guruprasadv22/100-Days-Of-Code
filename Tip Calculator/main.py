print("Welcome to Tip Calculator.")

totalBill = float(input("What was your total bill? $"))
splitBetween = int(input("How many people to split the bill? "))
tipPercent = float(
    input("What percentage of tip would you like to give? 10, 12 or 15? "))


totalAmount = totalBill + totalBill * (tipPercent / 100)
eachPerson = totalAmount / splitBetween


print("Each person should pay: $" + str(round(eachPerson, 1)))
