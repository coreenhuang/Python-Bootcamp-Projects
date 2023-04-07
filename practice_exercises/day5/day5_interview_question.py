# FizzBuzz

# Print numbers from 1 to 100
# Numbers divisable by 3 should print 'Fizz'
# Numbers divisable by 5 should print 'Buzz'
# Numbers divisable by 3 and 5 should print 'FizzBuzz'

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)