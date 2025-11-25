def factorial(n):
    if n < 0:
        return "Undefined for negative numbers"
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def digit_sum(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n
def menu():
    while True:
        print("\n--- Python Mini Calculator ---")
        print("1. Calculate factorial")
        print("2. Condense number to single digit")
        print("3. Check Armstrong number")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            num = int(input("Enter a number: "))
            print(f"Factorial of {num} is {factorial(num)}")
        elif choice == '2':
            num = int(input("Enter a number: "))
            print(f"Condensed digit sum of {num} is {digit_sum(num)}")
        elif choice == '3':
            num = int(input("Enter a number: "))
            if is_armstrong(num):
                print(f"{num} is an Armstrong number.")
            else:
                print(f"{num} is NOT an Armstrong number.")
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
menu()