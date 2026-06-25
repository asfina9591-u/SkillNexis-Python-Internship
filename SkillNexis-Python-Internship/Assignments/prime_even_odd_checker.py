def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter number: "))
print("Even/Odd:", "Even" if num % 2 == 0 else "Odd")
print("Prime:", "Yes" if is_prime(num) else "No")
