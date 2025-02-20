def is_prime(n):
    if n<2:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    else:
        for i in range(3, int(n**0.5)+1, 2):
            if n%i==0:
                return False
            return True
try:
    n=int(input("Enter a num: "))
    if is_prime(n):
        print("Your num is prime: ")
    else:
        print("Your num is not prime")
except:
    print("Data type is not correct")