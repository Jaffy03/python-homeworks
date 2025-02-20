def factors(n):
    num=n
    for i in range(1, n+1):
        if num%i==0:
            print(f"{i} is a factor of {num}")
    
try:
    num=int(input("Enter a positive integer: "))
    factors(num)
except:
    print("Data type is not correct")