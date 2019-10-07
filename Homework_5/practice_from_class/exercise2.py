numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def isPrime(num):
    if all(num%i != 0 for i in range(2,num)):
        return num

prime_numbers = list(map(isPrime, numbers))

def square_nums(num):
    if num == None:
        pass
    else:
        return num ** 2

square_numbers = list(map(square_nums, prime_numbers))

for n in square_numbers:
    if n == None:
        pass
    else:
        print(n)

