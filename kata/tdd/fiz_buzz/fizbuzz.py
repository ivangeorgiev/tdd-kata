def fizbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)

def fizbuzz1(n):
    divisors = ( (15, "FizzBuzz"), (3, "Fizz"), (5, "Buzz") )
    for divisor, result in divisors:
        if n % divisor == 0:
            return result
    return str(n)


from functools import reduce

def fizbuzz2(n):
    divisors = ( (3, "Fizz"), (5, "Buzz") )
    result = ""
    for divisor, word in divisors:
        if n % divisor == 0:
            result = result + word
    if result == "":
        result = str(n)
    return result

