def factorial(n, memo={}):
    """
    Calculate the factorial of a number using memoization.
    
    Args:
    n (int): The number to calculate the factorial for.
    memo (dict): A dictionary to store previously calculated factorials.
    
    Returns:
    int: The factorial of the number n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        memo[n] = 1
    else:
        memo[n] = n * factorial(n - 1, memo)
    return memo[n]

def main():
    try:
        number = int(input("Enter a number to find its factorial: "))
        result = factorial(number)
        print(f"The factorial of {number} is: {result}")
        print("Factorials calculated so far:", factorial.__defaults__[0])
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
