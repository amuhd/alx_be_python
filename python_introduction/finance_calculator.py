# prompt
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

# montly savings
monthly_savings = monthly_income - monthly_expenses

# yearly interest rate
annual_interest_rate = 0.05

# projected savings for a year
yearly_savings = monthly_savings * 12
projected_annual_savings = yearly_savings + (yearly_savings * annual_interest_rate)

# monthly savings
print(f'Your monthly savings are: ${monthly_savings}')

# projected annual savings
print(f'Projected savings after one year, with interest, is: ${projected_annual_savings}')
