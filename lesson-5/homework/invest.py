def invest(amount, rate, years):
    new_amount=amount
    for i in range(years):
        new_amount=new_amount+new_amount*rate
        print(f"year {i+1}: ${new_amount:.2f}")

try: 
    amount=float(input("Enter an initial amount: "))
    rate=float(input("Enter an annual percentage rate: "))
    years= int(input("Enter a number of years: "))
    invest(amount, rate, years)
except:
    print("Data type is not valid")