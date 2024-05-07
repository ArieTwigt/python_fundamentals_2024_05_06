# donations

total_donation_amount = 0
max_donation_amount = 1000


while total_donation_amount <= max_donation_amount:
    donation_amount = float(input("How much would you like to donate:\n"))

    total_donation_amount += donation_amount

    print(f"Total donation {total_donation_amount}")