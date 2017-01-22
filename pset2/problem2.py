balance = 3926
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12.0
minimumPayment = 10
enough = False

while not(enough):
    balanceTest = balance
    for i in range(12):
        balanceTest -= minimumPayment
        interest = monthlyInterestRate * balanceTest
        balanceTest += interest
    if balanceTest <= 0:
        enough = True
    else:
        minimumPayment += 10

print("Lowest Payment: " + str(minimumPayment))