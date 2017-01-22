def ccbalance(balance, annualInterestRate, monthlyPayment, numberOfMonths = 12):    
    """
    inputs:
        balance             - credit card balance at month 0
        annualInterestRate  - annual interest rate charged on balance
        monthlyPayment      - fixed amount paid each month
        numberOfMonths      - number of months to run calculation for
    returns:
        credit card balance (rounded to 2 decimal places) after numberOfMonths
    """

    unpaidBalance = balance
    for month in range(numberOfMonths):        
        unpaidBalance = (unpaidBalance - monthlyPayment) * (1.0 + annualInterestRate / 12.0)

    return round(unpaidBalance, 2)
 
def ccpayoff (balance, annualInterestRate, numberOfMonths = 12):
    """
    inputs:
        balance             - credit card balance at month 0
        annualInterestRate  - annual interest rate charged on balance
        numberOfMonths      - number of months to run calculation for
    returns:
        minimum fixed payment that is a multiple of 10 and that will pay off the
        credit card balance after numberOfMonths
    """
    
    unpaidBalance = balance;
    monthlyPayment = 0
    while unpaidBalance > 0:
        monthlyPayment += 10
        unpaidBalance = balance
        unpaidBalance = ccbalance(unpaidBalance, annualInterestRate, monthlyPayment, numberOfMonths)
        
    return monthlyPayment

#Test Case 1:
balance = 3329
annualInterestRate = 0.2
#Remove the test case above before using the automated grader
#Expected result:  Lowest Payment: 310
print("Lowest Payment: " + str(ccpayoff(balance, annualInterestRate)))