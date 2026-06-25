def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

n = int(input("Enter number: "))
print("Number is", check_even_odd(n))
