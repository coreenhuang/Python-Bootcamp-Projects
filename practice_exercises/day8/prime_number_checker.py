# Prime Number Checker

def prime_checker(number):
    count = 0
    for x in range(2,number):
        if number % x == 0:
            count += 1
    if count > 0:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")

# Alternative if statement logic

# is_prime = True
# if number % i == 0:
#   is_prime = False
# if is_prime: print ....

n = int(input("Check this number: "))
prime_checker(number=n)
