# Function to calculate monthly loan payments
def calculate_loan_payment(principal, interest_rate, loan_term_months):
    monthly_interest_rate = interest_rate / 100 / 12
    numerator = principal * monthly_interest_rate * (1 + monthly_interest_rate) ** loan_term_months
    denominator = (1 + monthly_interest_rate) ** loan_term_months - 1
    monthly_payment = numerator / denominator
    return monthly_payment

if __name__ == "__main__":
    print("Welcome to the Basic Loan Calculator!")

    try:
        principal = float(input("Enter the loan principal amount: $"))
        interest_rate = float(input("Enter the annual interest rate (%): "))
        loan_term_months = int(input("Enter the loan term in months: "))

        monthly_payment = calculate_loan_payment(principal, interest_rate, loan_term_months)

        print(f"Your monthly loan payment is: ${monthly_payment:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values for principal, interest rate, and loan term.")

