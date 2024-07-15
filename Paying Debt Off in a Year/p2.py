intst = annualInterestRate / 12
payment = 0
bal = 1
while bal > 0:
    bal = balance
    payment += 10
    for i in range(12):
        bal = ((bal - payment) * (1 + intst))
print("Lowest Payment: {:0.2f}".format(payment))