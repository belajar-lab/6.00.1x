mnthInt = annualInterestRate/12
for i in range(12):
    balance *= (1 - monthlyPaymentRate) * (1 + mnthInt)
print("Remaining balance: {:0.2f}".format(balance))