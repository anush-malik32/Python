valid = False
while valid is False:
    try:
        bill = float(input("How much is your bill?"))
        discount = float(input("How much of a discount do you have?"))
        number = int(input("How many people are in you group?"))
        if number > 0 and bill > 0 and discount >= 0:
            valid = True
        print("Each person has to pay: $", ((discount/100)*bill)/number)                
    except ValueError:
        print("Input is not valid. Please try again.")
        valid = False
    except ZeroDivisionError:
        print("People cannot be Zero. Please try again.")
        valid = False