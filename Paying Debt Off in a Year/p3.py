lower = 0
upper = (balance * (1 + annualInterestRate/12)**12)/12.0
while True:
    bal = balance
    payment = (lower + upper) / 2
    for i in range(12):
        bal = ((bal - payment) * (1 + annualInterestRate/12))
    if bal < -0.1:
        upper = payment
    elif bal > 0.1:
        lower = payment
    else:
        break
print("Lowest: {:0.2f}".format(payment))