def calculate_factorial(n):
    
   
    if not isinstance(n, int):
        return "Error: Input must be an integer."

   
    if n < 0:
        return "Error: Factorial does not exist for negative numbers."

   
    if n == 0:
        return 1

   
    result = 1
    for i in range(1, n + 1):
        result *= i
    
    return result


if _name_ == "_main_":
    try:
       
        user_input = int(input("Enter a number to calculate factorial: "))
        
       
        print(f"The factorial of {user_input} is: {calculate_factorial(user_input)}")
        
    except ValueError:
        print("Invalid input! Please enter a whole number.")