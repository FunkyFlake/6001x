balance = 467
annualInterestRate = 0.2
monthlyPaymentRate = 0.08

monthlyInterestRate = annualInterestRate / 12.0

for i in range(12):
    minimumPayment = balance * monthlyPaymentRate
    balance -= minimumPayment
    interest = monthlyInterestRate * balance
    balance += interest

balance = round(balance, 2)
print("Remaining balance: " + str(balance))