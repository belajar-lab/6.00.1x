## Introduction

Each month, a credit card statement will come with the option for you to pay a minimum amount of your charge, usually 2\% of the balance due. However, the credit card company earns money by charging interest on the balance that you don't pay. So even if you pay credit card payments on time, interest is still accruing on the outstanding balance.

Say you've made a \$5,000 purchase on a credit card with an 18\% annual interest rate and a 2\% minimum monthly payment rate. If you only pay the minimum monthly amount for a year, how much is the remaining balance?

You can think about this in the following way.

At the beginning of month 0 (when the credit card statement arrives), assume you owe an amount we will call $b_0$ ($b$ for *balance*; subscript $0$ to indicate this is the balance at month $0$).

Any payment you make during that month is deducted from the balance. Let's call the payment you make in month 0, $p_0$. Thus, your **unpaid balance** for month 0, $ub_0$, is equal to $b_0 - p_0$.

$$
ub_0 = b_0 - p_0
$$

At the beginning of month 1, the credit card company will charge you interest on your unpaid balance. So if your annual interest rate is $r$, then at the beginning of month 1, your new balance is your previous unpaid balance $ub_0$, **plus** the interest on this unpaid balance for the month. In algebra, this new balance would be

$$
b_1 = ub_0 + \frac{r}{12.0}\cdot ub_0
$$

In month 1, we will make another payment, $p_1$. That payment has to cover some of the interest costs, so it does not completely go towards paying off the original charge. The balance at the beginning of month 2, $b_2$, can be calculated by first calculating the unpaid balance after paying $p_1$, then by adding the interest accrued:

$$
ub_1 = b_1 - p_1\\
b_2 = ub_1 + \frac{r}{12.0} \cdot ub_1
$$

If you choose just to pay off the minimum monthly payment each month, you will see that the compound interest will dramatically reduce your ability to lower your debt.

Let's look at an example. If you've got a \$5,000 balance on a credit card with 18\% annual interest rate, and the minimum monthly payment is 2\% of the current balance, we would have the following repayment schedule if you only pay the minimum payment each month:

| Month | Balance | Minimum Payment | Unpaid Balance | Interest |
| --- | --- | --- | --- | --- |
| 0 | 5000.00 | 100 (= 5000 * 0.02) | 4900 (= 5000 - 100) | 73.50 (= 0.18/12.0 * 4900) |
| 1 | 4973.50 (= 4900 + 73.50) | 99.47 (= 4973.50 * 0.02) | 4874.03 (= 4973.50 - 99.47) | 73.11 (= 0.18/12.0 * 4874.03) |
| 2 | 4947.14 (= 4874.03 + 73.11) | 98.94 (= 4947.14 * 0.02) | 4848.20 (= 4947.14 - 98.94) | 72.72 (= 0.18/12.0 * 4848.20) |

You can see that a lot of your payment is going to cover interest, and if you work this through month 12, you will see that after a year, you will have paid \$1165.63 and yet you will still owe \$4691.11 on what was originally a \$5000.00 debt. Pretty depressing!

## Problem 1
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

1. `balance` - the outstanding balance on the credit card
2. `annualInterestRate` - annual interest rate as a decimal
3. `monthlyPaymentRate` - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print

```
Remaining balance: 813.41
```

instead of

```
Remaining balance: 813.4141998135
```

So your program only prints out one thing: the remaining balance at the end of the year in the format:

```
Remaining balance: 4784.0
```

A summary of the required math is found below:

> Monthly interest rate= (Annual interest rate) / 12.0
> 
> 
> **Minimum monthly payment** = (Minimum monthly payment rate) x (Previous balance)
> 
> **Monthly unpaid balance** = (Previous balance) - (Minimum monthly payment)
> 
> **Updated balance each month** = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
> 

## Test cases

---

We provide sample test cases below. Make sure your code passes the sample test cases.

**Note:** Depending on where you round in this problem, your answers may be off by a few cents in either direction.

```
# Test Case 1:
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# Result Your Code Should Generate Below:
Remaining balance: 31.38

# To make sure you are doing calculation correctly, this is the
# remaining balance you should be getting at each month for this example
Month 1 Remaining balance: 40.99
Month 2 Remaining balance: 40.01
Month 3 Remaining balance: 39.05
Month 4 Remaining balance: 38.11
Month 5 Remaining balance: 37.2
Month 6 Remaining balance: 36.3
Month 7 Remaining balance: 35.43
Month 8 Remaining balance: 34.58
Month 9 Remaining balance: 33.75
Month 10 Remaining balance: 32.94
Month 11 Remaining balance: 32.15
Month 12 Remaining balance: 31.38
```

```
Test Case 2:
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

Result Your Code Should Generate Below:
Remaining balance: 361.61
```

>💡 **Only two decimal digits of accuracy?** 
> Use the [`round`](http://docs.python.org/library/functions.html#round) function at the end of your code!

>💡 **How to think about this problem?**
>To help you get started, here is a rough outline of the stages you should probably follow in writing your code:
>
>- For each month:
>    - Compute the monthly payment, based on the previous month’s balance.
>    - Update the outstanding balance by removing the payment, then charging interest on the result.
>    - Output the month, the minimum monthly payment and the remaining balance.
>    - Keep track of the total amount of paid over all the past months so far.
>- Print out the result statement with the total amount paid and the remaining balance.
>
>Use these ideas to guide the creation of your code.