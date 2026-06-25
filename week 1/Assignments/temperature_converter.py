def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

choice = input("Convert to (C/F): ").upper()
temp = float(input("Enter temperature: "))

if choice == "F":
    print("In Fahrenheit:", celsius_to_fahrenheit(temp))
elif choice == "C":
    print("In Celsius:", fahrenheit_to_celsius(temp))
else:
    print("Invalid choice")
