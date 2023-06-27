print("Tip Calculator")

print()

choice = "y"
while choice.lower() == "y":  
    # get user input

    cost = float(input("Cost of meal: \t"))

    #15%
    tip = round(cost * 0.15, 2)
    total = round(tip + cost, 2)
    print("15%")
    tip = float(input("Tip amount: \t"))
    print("Total amount: \t", total)
    print()

    #20%
    tip = round(cost * 0.20, 2)
    total = round(tip + cost, 2)
    print("20%")
    tip = float(input("Tip amount: \t"))
    print("Total amount: \t", total)
    print()

    #25%
    tip = round(cost * 0.25, 2)
    total = round(tip + cost, 2)
    print("25%")
    tip = float(input("Tip amount: \t"))
    print("Total amount: \t", total)
    print()

    #test if user wants to continue
    choice = input("Continue (y/n)?: ")
    print()
    
print("Bye!")