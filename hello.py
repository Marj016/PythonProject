import math

text = ("Reimann Zeta Function ζ(s) from s=1 to s=10 where n=10")
print(text.capitalize)

def riemann_zeta(s, n=10):
    """
    Calculate the Riemann zeta function using the series definition.
    
    Parameters:
    s (complex): The complex argument for the zeta function.
    n (int): The value of n to sum in the series (default is 10).
    
    Returns:
    complex: The exact value of the Riemann zeta function at s.
    """
    zeta_value = 0
    for n in range(1, n + 1):
        zeta_value += 1 / (n ** s)
    return zeta_value

# Example usage:
s = 2  # For real values of s
result = riemann_zeta(s)
print(f"Riemann zeta function ζ(s) at s = 2 with n = 10: {result}")

def compute_zeta_3(n):
    """
    Compute the sum for zeta(3) using the formula:
    sum_({n=1}^{N} \frac{3n + 2}{n^2(n+1)(n+2)}) 

    Args:
        n (int): Value of n to include in the summation.
    
    Returns:
        float: Exact value of the series.
    """

    total_sum = 0 
    for n in range(1, n + 1):
        numerator = 3 * n + 2
        denominator = n**2 * (n + 1) * (n + 2)
        total_sum += numerator / denominator
    return total_sum

def riemann_zeta_3(n):
    return sum(1 / (i ** 3) for i in range(1, n + 1))

n = 10
exact_value = riemann_zeta_3(n)
print(f"Riemann zeta function ζ(s) at s = 3 with n = {n}: {exact_value}")

def compute_zeta_4(n):
    """
    Compute the sum for zeta(4) using the formula:
    sum_({n=1}^{N} \frac{3n + 2}{n^2(n+1)(n+2)}) 

    Args:
        n (int): Value of n to include in the summation.
    
    Returns:
        float: Exact value of the series.
    """

    total_sum = 0 
    for n in range(1, n + 1):
        numerator = 3 * n + 2
        denominator = n**2 * (n + 1) * (n + 2)
        total_sum += numerator / denominator
    return total_sum

def riemann_zeta_4(n):
    return sum(1 / (i ** 4) for i in range(1, n + 1))

n = 10
exact_value = riemann_zeta_4(n)
print(f"Riemann zeta function ζ(s) at s = 4 with n = {n}: {exact_value}")

def compute_zeta_5(n):
    """
    Compute the sum for zeta(5) using the formula:
    sum_({n=1}^{N} \frac{3n + 2}{n^2(n+1)(n+2)}) 

   Args:
        n (int): Value of n to include in the summation. 
    
    Returns:
        float: Exact value of the series.
    """

    total_sum = 0 
    for n in range(1, n + 1):
        numerator = 3 * n + 2
        denominator = n**2 * (n + 1) * (n + 2)
        total_sum += numerator / denominator
    return total_sum

def riemann_zeta_5(n):
    return sum(1 / (i ** 5) for i in range(1, n + 1))

n = 10
exact_value = riemann_zeta_5(n)
print(f"Riemann zeta function ζ(s) at s = 5 with n = {n}: {exact_value}")

def compute_zeta_6(n):
    """
    Compute the sum for zeta(6) using the formula:
    sum_({n=1}^{N} \frac{3n + 2}{n^2(n+1)(n+2)}) 

    Args:
        n (int): Value of n to include in the summation.
    
    Returns:
        float: Exact value of the series.
    """

    total_sum = 0 
    for n in range(1, n + 1):
        numerator = 3 * n + 2
        denominator = n**2 * (n + 1) * (n + 2)
        total_sum += numerator / denominator
    return total_sum

def riemann_zeta_6(n):
    return sum(1 / (i ** 6) for i in range(1, n + 1))

n = 10
exact_value = riemann_zeta_6(n)
print(f"Riemann zeta function ζ(s) at s = 6 with n = {n}: {exact_value}")

def compute_zeta_7(n):
    """
    Compute the sum for zeta(7) using the formula:
   sum_({n=1}^{N} \frac{3n + 2}{n^2(n+1)(n+2)}) 

    Args:
        n (int): Value of n to include in the summation. 
    
    Returns:
        float: Exact Value of the series.
    """

    total_sum = 0 
    for n in range(1, n + 1):
        numerator = 3 * n + 2
        denominator = n**2 * (n + 1) * (n + 2)
        total_sum += numerator / denominator
    return total_sum

def riemann_zeta_7(n):
    return sum(1 / (i ** 7) for i in range(1, n + 1))

n = 10
exact_value = riemann_zeta_7(n)
print(f"Riemann zeta function ζ(s) at s = 7 with n = {n}: {exact_value}")

def compute_zeta_8(n):
    """
    Compute the sum for zeta(8) using the formula:
    sum_({n=1}^{N} \frac{3n + 2}{n^2(n+1)(n+2)}) 

   Args:
        n (int): Value of n to include in the summation.
    
    Returns:
        float: Exact value of the series.
    """

    total_sum = 0 
    for n in range(1, n + 1):
        numerator = 3 * n + 2
        denominator = n**2 * (n + 1) * (n + 2)
        total_sum += numerator / denominator
    return total_sum

def riemann_zeta_8(n):
    return sum(1 / (i ** 8) for i in range(1, n + 1))

n = 10
exact_value = riemann_zeta_8(n)
print(f"Riemann zeta function ζ(s) at s = 8 with n = {n}: {exact_value}")

def compute_zeta_9(n):
    """
    Compute the sum for zeta(9)) using the formula:
   sum_({n=1}^{N} \frac{3n + 2}{n^2(n+1)(n+2)}) 

Args:
        n (int): Value of n to include in the summation. 
    
    Returns:
        float: Exact value of the series.
    """

    total_sum = 0 
    for n in range(1, n + 1):
        numerator = 3 * n + 2
        denominator = n**2 * (n + 1) * (n + 2)
        total_sum += numerator / denominator
    return total_sum

def riemann_zeta_9(n):
    return sum(1 / (i ** 9) for i in range(1, n + 1))

n = 10
exact_value = riemann_zeta_9(n)
print(f"Riemann zeta function ζ(s) at s = 9 with n = {n}: {exact_value}")

def compute_zeta_10(n):
    """
    Compute the sum for zeta(10) using the formula:
    sum_({n=1}^{N} \frac{3n + 2}{n^2(n+1)(n+2)}) 

   Args:
        n (int): Value of n to include in the summation.
    
    Returns:
        float: Exact value of the series.
    """

    total_sum = 0 
    for n in range(1, n + 1):
        numerator = 3 * n + 2
        denominator = n**2 * (n + 1) * (n + 2)
        total_sum += numerator / denominator
    return total_sum

def riemann_zeta_10(n):
    return sum(1 / (i ** 10) for i in range(1, n + 1))

n = 10
exact_value = riemann_zeta_10(n)
print(f"Riemann zeta function ζ(s) at s = 10 with n = {n}: {exact_value}")