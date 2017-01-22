def ccbalance(balance, annualInterestRate, monthlyPayment, numberOfMonths=12):
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
        minimum fixed payment that is a multiple of 10 and that will pay off
        the credit card balance after numberOfMonths
    """

    unpaidBalance = 0
    monthlyPayment = 0
    lowerBoundPayment = balance / numberOfMonths
    upperBoundPayment = (balance * (1 + annualInterestRate) ** numberOfMonths) / numberOfMonths

    while True:
        monthlyPayment = (upperBoundPayment + lowerBoundPayment) / 2
        unpaidBalance = ccbalance(balance, annualInterestRate, monthlyPayment, numberOfMonths)

        if unpaidBalance > -0.001 and unpaidBalance <= 0:
            break
        elif unpaidBalance < 0:
            upperBoundPayment = monthlyPayment
        else:
            lowerBoundPayment = monthlyPayment

    return monthlyPayment

#Test Case 1:
balance = 320000
annualInterestRate = 0.2
#Remove or comment out the above test case before submitting this code to the automated grader.
#Expected result: Lowest Payment: 29157.09
print("Lowest Payment: " + str(round(ccpayoff(balance, annualInterestRate), 2)))
