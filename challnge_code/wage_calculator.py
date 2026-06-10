def get_hours_worked():
    while True:
        try:
            input_value = float(input("Enter the number of hours worked daily: "))
            if (input_value <= 0) or (input_value > 24):
                print("ERROR: Hours worked must be greater than 0 and less than 24\n")
                continue
            break
        except ValueError:
            print("ERROR: Please enter a numerical value.\n")
            continue
    
    return input_value

def get_hourly_wage():
    while True:
        try:
            input_value = float(input("Enter hourly wage: "))
            if (input_value <= 0):
                print("ERROR: Hourly wage must be greater than 0\n")
                continue
            break
        except ValueError:
            print("ERROR: Please enter a numerical value.\n")
            continue
    
    return input_value

def main():
    #declare known variable values
    #12% tax rate
    tax_rate = 0.12
    days_worked = 350
    another_calculation = True
    
    #ask user for number of hours worked daily by calling the get_nonnegative_float_from_user function
    hours = get_hours_worked()

    #ask user for hourly wage by calling the get_nonnegative_float_from_user function
    hourly_wage = get_hourly_wage()

    #calculate annual wage
    annual_wage = hours * hourly_wage * days_worked

    #calculate tax amount
    tax_amount = tax_rate * annual_wage

    #calculate annual wage minus tax
    annual_wage_minus_tax = annual_wage - tax_amount

    #output results
    print(f"\nPay Advice")
    print(f"-------------")
    print(f"Hours Worked: {hours}")
    print(f"Hourly Wage: ${hourly_wage}")
    print(f"Wages Before Taxes: ${annual_wage:,.2f}")
    print(f"Tax Amount: ${tax_amount:,.2f}")
    print(f"Annual Wage After Taxes: ${annual_wage_minus_tax:,.2f}")

main()
    
