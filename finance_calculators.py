# Lesson SE-T12
# Task 1


# finance_calculators.py--a program that allows the user to access two different 
#   financial calculators: an investment and a loan repayment calculator.


import math

# Display menu
print("""
        ********************************************************************************* 

        Choose either 'investment' or 'loan' from the menu below to proceed:
        
        investment  -  to calculate the amount of interest you'll earn on your investment
        loan       -  to calculate the amount you'll have to pay on a home loan 
        
        *********************************************************************************
        """)


# Request the user to enter a choice from the menu
choice = str.lower(input("\tPlease enter your choice: "))


# Verify the input is matching the menu, if not display error message and prompt user to re-enter choice
if choice != "investment" and choice != "loan":
    choice = str.lower(input("\tError: option does not exist! Please enter investment or loan: "))


# Evaluate which financial instrument was chosen and prompt the user to provide relevant information
if choice == "investment":
    deposit_amount = float(input("\tHow much would you like to deposit: "))
    interest_rate = float(input("\tWhat is the interest rate:      %\b\b\b\b\b\b"))
    invest_duration = int(input("\tHow many years are you planning to hold this investment: "))
    interest = str.lower(input("\tPlease enter your preference of simple or compound interest: "))

    if interest != "simple"  and interest != "compound" :            # Verify the input is matching options
        interest = str.lower(input("\tError: option does not exist! Please enter simple or compound: "))
        
    if interest == "simple":            

        # Calculate the return of simple interest for the investment
        total_amount = deposit_amount * ( 1 + (interest_rate / 100) * invest_duration )
        amount_earned = total_amount - deposit_amount

        # Display results of the calculation
        print(f"""
        *********************************************************************************
                                                                                           
             The total amount you will earn from an investment of {deposit_amount} with             
             an interest rate of {interest_rate}% (simple interest) and a duration 
             of {int(invest_duration)} years will be {round(amount_earned, 2)}                                                
                                                                                         
        *********************************************************************************
        """)

    elif interest == "compound":          

        # Calculate the return of compound interest for the investment
        total_amount = deposit_amount * math.pow( 1 + (interest_rate / 100 ), invest_duration )
        amount_earned = total_amount - deposit_amount

        # Display results of the calculation
        print(f"""
        *********************************************************************************
                                                                                           
             The total amount you will earn from an investment of {deposit_amount} with             
             an interest rate of {interest_rate}% (compounding interest) and a duration 
             of {int(invest_duration)} years will be {round(amount_earned, 2)}                                                
                                                                                         
        *********************************************************************************
        """)

elif choice == "loan":
    loan_amount = float(input("\tHow much would you like to borrow: "))
    interest_rate = float(input("\tWhat is the interest rate:      %\b\b\b\b\b\b"))
    payment_duration = float(input("\tIn how many month's would you like to repay the loan: "))

    # Calculate the monthly payments of the loan
    rate = interest_rate / 100
    monthly_payment = loan_amount * (rate / 12) * (1/(1-(1+(rate / 12))**(-payment_duration))) 
    
    # Display results of the calculation
    print(f"""
        ********************************************************************************
         
             A loan of {loan_amount} with an interest rate of {interest_rate}% and a duration 
             of {int(payment_duration)} months equates to a monthly payment of {round(monthly_payment, 2)}
          

        ********************************************************************************
        """)


