target_num = 600851475143

def prime_factors(num):
  primes = []

  while num % 2 == 0:
    primes.append(2)
    num = num / 2


