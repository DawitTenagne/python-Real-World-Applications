def isprime(num):
    """The function isprime() takes in as a parameter a
    single integer, and returns either True or False."""
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
    return prime