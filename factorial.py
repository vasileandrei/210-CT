def factorial(n):
    """calculates the factorial of the number inputed"""
    
    if n < 0:
        raise ValueError("Number cannot be less than 0")
    if n == 0 or n == 1:
        return (1)
    else:
        number = n * factorial(n-1)
        return (number)
