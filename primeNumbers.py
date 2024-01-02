
'''
                        Listing prime numbers up to the value we enter.

              A prime number (or a prime) is a natural number greater than 1 that
            is not a product of two smaller natural numbers. A natural number greater than 1
            that is not prime is called a composite number. For example, 5 is prime because
            the only ways of writing it as a product, 1 × 5 or 5 × 1, involve 5 itself.
            However, 4 is composite because it is a product (2 × 2) in which both numbers are
            smaller than 4.

'''

# we check prime numbers
def primeCheck(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# i add prime numbers to the empty list up to the entered value
def primeNumbers(x):
    primeNumbersList = []
    for i in range(2, x):
        if primeCheck(i):
            primeNumbersList.append(i)
    return primeNumbersList

x = int(input('Value : '))
print('Prime Numbers up to', x, ':', primeNumbers(x))

