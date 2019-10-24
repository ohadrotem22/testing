fib = []
def fibon(number = input("How many Fibonacci numbers to print? ")):
    number = int(number)
    if number == 0:
        fib = []
    elif number == 1:
        fib = [1]
    elif number == 2:
        fib = [1, 1]
    elif number > 2:
        fib = [1, 1]
        for i in range(1, number - 1):
            num = fib[i] + fib[(i - 1)]
            fib += [num]
        return fib
print(fibon())
