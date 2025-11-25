def condense_number(n):
    """
Condenses a positive integer into a single digit (Digital Root).

    Args:
n: The number to condense. Can be passed as an integer or a string.
    Returns:
        The single-digit digital root (0-9), or an error message if input is invalid.
    """
    try:
        n_int = int(n)
    except ValueError:
        return "Invalid input. Please enter a valid integer."
    
    if n_int < 0:
        return "Error: The digital root is defined for non-negative numbers."

    if n_int == 0:
        return 0
    
    digital_root = n_int % 9
    
    return 9 if digital_root == 0 else digital_root


num1 = 1984
result1 = condense_number(num1)
print(f"The condensed single digit for {num1} is: {result1}") 

num2 = 81
result2 = condense_number(num2)
print(f"The condensed single digit for {num2} is: {result2}") 

num3 = 456
result3 = condense_number(num3)
print(f"The condensed single digit for {num3} is: {result3}")