import math
intro = """
**********************************************************
FINANCE CALCULATOR

This calculator will the value of an investment after a 
given number of years or the value of a home repayments. 

These are defined as:
    Investment - to calculate the amount of interest you'll 
    earn on your investment 
    Bond - to calculate the amount you'll have to pay on a home loan

**********************************************************
"""
# print information to user, take user input for investment type
print(intro)

# following block will only run if user has input investment, with nested conditional block to branch off into simple or compound interest
while True:
    finance = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
    if finance == "investment":
        
        while True:
            amount = (input("Amount: ")).strip("£")
            if amount.isnumeric():
                    amount = float(amount)
                    break
            else:
                print("That is not a valid amount, try again.")

        while True:
            percent = (input("Interest rate: ")).strip("%")
            if percent.replace(".", "").isnumeric():
                percent = float(percent)
                break
            else:
                print("That is not a valid interese rate, try again.")
        
        while True:
            years = input("Number of years: ")
            if years.isnumeric():
                years = int(years)
                break
            else:
                print("That is not a valid number of years. Try again.")


        while True:
            interest = input("Simple or compound interest? ").lower()
            if interest == "simple":
                final = (percent/100 * amount * years) + amount
                break
            elif interest == "compound":
                final = round((amount*(1+percent/100)**years),2)
                break
            else:
                print("That is not a valid interest type. Try again.")
        print(f"Your {finance} will be worth £{final}")
        break
    # following block will only run it user has input bond.
    elif finance == "bond":
        while True:
            value = input("House value: ")
            if value.isnumeric():
                value = float(value)
                break
            else:
                print("That is not a valie house value. Try again.")
        
        while True:
            interest = input("Interest rate: ")
            if interest.replace(".", "").isnumeric():
                interest = float(interest)
                break
            else:
                print("That is not a valid interest rate. Try again.")
        
        while True:
            months = input("Number of months: ")
            if months.isnumeric():
                months = int(months)
                break
            else:
                print("That is not a valid amount of months. Try again.")

        final = (interest * value)/(1 - (1 + interest)**(-months))

        repayment = round((final / months),2)

        print(f"""
**********************************************************
Your monthly repayments wil be £{repayment}
**********************************************************
              """)
        break

    else:
        print("That is not a valid investment type. Try again.")
