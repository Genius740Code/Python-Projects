def investment_calculator(principal, rate, time, monthly_contribution, show_every_5_months=False):
    for month in range(1, time + 1):
        principal = principal * (1 + rate / 100) + monthly_contribution

        if show_every_5_months and month % 5 == 0:
            print(f"Amount after {month} months: {principal:.2f}")

    return principal

principal = float(input("Enter the initial amount in the account: "))
rate = float(input("Enter the annual interest rate (in percentage): "))
time = int(input("Enter the number of months the money will be invested: "))
monthly_contribution = float(input("Enter the monthly contribution: "))
show_every_5_months = input("Do you want to display the amount every 5 months? (y/n): ").lower() == 'y'

result = investment_calculator(principal, rate, time, monthly_contribution, show_every_5_months)
print(f"The future value of the investment after {time} months is: {result:.2f}")
