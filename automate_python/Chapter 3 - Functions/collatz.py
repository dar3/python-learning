def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result


print("Enter a number")
number = int(input())
while number != 1:
    number = collatz(number)