# 7▹ Stwórz moduł, który dla dowolnej wartości n, zwróci ciąg fibonnaciego.


def fibonacci(n):
    number1 = 0
    number2 = 1
    count = 0
    if n <=0:
        print("the number must be higher than 0")
    elif n == 1:
        print(f"Fibonacci sequence for {n} is {number1}")
    else:
        print(f"Fibonacci sequence for {n} is:")
        while count < n:
            print(number1)
            result = number1 +number2
            number1 = number2
            number2 = result
            count += 1




