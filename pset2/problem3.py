balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate / 12.0
lowerBound = balance / 12
upperBound = (balance * (1 + monthlyInterestRate) ** 12) / 12.0

while True:
    balanceTest = balance
    payment = (upperBound + lowerBound) / 2
    for i in range(12):
        balanceTest -= payment
        interest = monthlyInterestRate * balanceTest
        balanceTest += interest
    if abs(balanceTest) <= 0.05:
        print("Lowest Payment: " + str(round(payment,2)))
        break
    elif balanceTest > 0:
        lowerBound = payment
    elif balanceTest < 0:
        upperBound = payment
