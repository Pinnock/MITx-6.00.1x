def ccbalance(balance, annualInterestRate, monthlyPaymentRate):
    '''
    Author:         Rayon Pinnock
    Date:           January 20, 2017
    Description:    Calculates the credit card balance after one
                    year if a person only pays the minimum
                    monthly payment required by the credit card
                    company each month.
    Inputs:
        balance - the outstanding balance on the credit card
        annualInterestRate - annual interest rate as a decimal
        monthlyPaymentRate - minimum monthly payment rate as a
        decimal

    Returns:
        The credit card balance remaining after 1 year
    '''
    numberOfMonths = 12
    for month in range(numberOfMonths):
        unpaidBalance = balance * (1 - monthlyPaymentRate)
        interest = unpaidBalance * annualInterestRate / 12
        balance = unpaidBalance + interest
    
    return round(balance, 2)

# Test Case 1:
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
#Remove or comment out the above test case before submitting this code to the automated grader.
#Expected result: Remaining balance: 31.38

print("Remaining balance: " + str(round(ccbalance(balance, annualInterestRate, monthlyPaymentRate), 2)))