principle_amount = int(input("Principle Amount : "))
interest = int(input(" Vaddi Rupees : "))
time = int(input("Time Period in Months : "))

interest_per_month = (principle_amount/100)*interest
total_interest = interest_per_month*time
total_return = principle_amount+total_interest

print("\nInterest Per Month = ",interest_per_month)
print("\nTotal Interest = ",total_interest)
print("\nTotal Return = ",total_return)
