import math

text = 'Calculating the approximate values of Riemann zeta function from s=1 to s=10 where n = 1000'
print(text)
# Add a space for a new paragraph
print("\n")  # This will create a blank line

#Calculate the exact value of the series for harmonic series which is ζ(1) using 1000 terms 

def harmonic_sum(n):
    """
    Calculate the sum for ζ(1) using the formula:
    sum_({n=1}^N \frac{3n + 2}{n^2(n+1)(n+2)})

    Args:
        n (int): Value of n include in the summation. 
    
    Returns:
        float: Exact values of the series
    """

    total_sum = 0
    for n in range(1, (n +1)):
        numerator = 3 * n + 2
        denominator = n**2 * (n + 1) * (n + 2)
        total_sum += numerator / denominator 
    return total_sum

def harmonic_sum(n):
    return sum(1 / i for i in range(1, n + 1))

n = 1000
exact_value = harmonic_sum(n)
print (f"ζ(s) at s = 1 with n = {n}: {exact_value}")

# Compute the exact values of the series for ζ(2) where n = 1000

def compute_zeta_2(n):
    """
    Compute the sum for ζ(2) using the formula:
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

def riemann_zeta_2(n):
    return sum(1 / (i ** 2) for i in range(1, n + 1))

n = 1000
exact_value = riemann_zeta_2(n)
print(f"ζ(s) at s = 2 with n = {n}: {exact_value}")

#Calculate the exact value of the series of the Riemann zeta function ζ(s) at s = 3 using 1000 terms 

def calculate_zeta_3(n):
    """
    Calculate the sum for zeta(3) using the formula:
    sum_({n=1}^{N} \frac{3n +2}{n^2(n+1)(n+2)})

    Args:
        n (int): Value of n to include in the summation.
    
    Returns:
        float: Exact value of the series.
    """

    total_sum = 0 
    for n in range(1, (n + 1)):
        numerator  = 3 * n + 2
        denominator = n**2 * (n + 1) * (n + 2)
        total_sum += numerator / denominator
    return total_sum

def riemann_zeta_3(n):
    return sum(1 / (i ** 3) for i in range(1, n + 1))

n = 1000
exact_value = riemann_zeta_3(n)
print(f"ζ(s) at s = 3 with n = {n}: {exact_value}")

def calculate_zeta_4(n):
    """
    Calculate the sum for zeta(4) using the formula:
    sum_({n=1}^{N} \frac{3n +2}{n^2(n+1)(n+2)})

    Args:
        n (int): Exact value of n to include in the summation.
    
    Returns:
        float: Exact value of the series.
    """

    total_sum = 0 
    for n in range(1, (n + 1)):
        numerator  = 3 * n + 2
        denominator = n**2 * (n + 1) * (n + 2)
        total_sum += numerator / denominator
    return total_sum

def riemann_zeta_4(n):
    return sum(1 / (i ** 4) for i in range(1, n + 1))

n = 1000
exact_value = riemann_zeta_4(n)
print(f"ζ(s) at s = 4 with n = {n}: {exact_value}")

def calculate_zeta_5(n):
    """
    Calculate the sum for zeta(5) using the formula:
    sum_({n=1}^{N} \frac{3n +2}{n^2(n+1)(n+2)})

    Args:
        n (int): Value of n to include in the summation.
    
    Returns:
        float: Exact value of the series.
    """

    total_sum = 0 
    for n in range(1, (n + 1)):
        numerator  = 3 * n + 2
        denominator = n**2 * (n + 1) * (n + 2)
        total_sum += numerator / denominator
    return total_sum

def riemann_zeta_5(n):
    return sum(1 / (i ** 5) for i in range(1, n + 1))

n = 1000
exact_value = riemann_zeta_5(n)
print(f"ζ(s) at s = 5 with n = {n}: {exact_value}")

def calculate_zeta_6(n):
    """
    Calculate the sum for zeta(6) using the formula:
    sum_({n=1}^{N} \frac{3n +2}{n^2(n+1)(n+2)})

    Args:
        n (int): Value of n to include in the summation.
    
    Returns:
        float: Exact value of the series.
    """

    total_sum = 0 
    for n in range(1, (n + 1)):
        numerator  = 3 * n + 2
        denominator = n**2 * (n + 1) * (n + 2)
        total_sum += numerator / denominator
    return total_sum

def riemann_zeta_6(n):
    return sum(1 / (i ** 6) for i in range(1, n + 1))

n = 1000
exact_value = riemann_zeta_6(n)
print(f"ζ(s) at s = 6 with n = {n}: {exact_value}")

def calculate_zeta_7(n):
    """
    Calculate the sum for zeta(7) using the formula:
    sum_({n=1}^{N} \frac{3n +2}{n^2(n+1)(n+2)})

    Args:
        n (int): Value of n to include in the summation.
    
    Returns:
        float: Exact value of the series.
    """

    total_sum = 0 
    for n in range(1, (n + 1)):
        numerator  = 3 * n + 2
        denominator = n**2 * (n + 1) * (n + 2)
        total_sum += numerator / denominator
    return total_sum

def riemann_zeta_7(n):
    return sum(1 / (i ** 7) for i in range(1, n + 1))

n = 1000
exact_value = riemann_zeta_7(n)
print(f"ζ(s) at s = 7 with n = {n}: {exact_value}")

def calculate_zeta_8(n):
    """
    Calculate the sum for zeta(8) using the formula:
    sum_({n=1}^{N} \frac{3n +2}{n^2(n+1)(n+2)})

    Args:
        n (int): Value of n to include in the summation.
    
    Returns:
        float: Exact value of the series.
    """

    total_sum = 0 
    for n in range(1, (n + 1)):
        numerator  = 3 * n + 2
        denominator = n**2 * (n + 1) * (n + 2)
        total_sum += numerator / denominator
    return total_sum

def riemann_zeta_8(n):
    return sum(1 / (i ** 8) for i in range(1, n + 1))

n = 1000
exact_value = riemann_zeta_8(n)
print(f"ζ(s) at s = 8 with n = {n}: {exact_value}")

def calculate_zeta_9(n):
    """
    Calculate the sum for zeta(9) using the formula:
    sum_({n=1}^{N} \frac{3n +2}{n^2(n+1)(n+2)})

    Args:
        n (int): Value of n to include in the summation.
    
    Returns:
        float: Exact value of the series.
    """

    total_sum = 0 
    for n in range(1, (n + 1)):
        numerator  = 3 * n + 2
        denominator = n**2 * (n + 1) * (n + 2)
        total_sum += numerator / denominator
    return total_sum

def riemann_zeta_9(n):
    return sum(1 / (i ** 9) for i in range(1, n + 1))

n = 1000
exact_value = riemann_zeta_9(n)
print(f"ζ(s) at s = 9 with n = {n}: {exact_value}")

def calculate_zeta_10(n):
    """
    Calculate the sum for zeta(10) using the formula:
    sum_({n=1}^{N} \frac{3n +2}{n^2(n+1)(n+2)})

    Args:
        n (int): Value of n to include in the summation.
    
    Returns:
        float: Exact value of the series.
    """

    total_sum = 0 
    for n in range(1, (n + 1)):
        numerator  = 3 * n + 2
        denominator = n**2 * (n + 1) * (n + 2)
        total_sum += numerator / denominator
    return total_sum

def riemann_zeta_10(n):
    return sum(1 / (i ** 10) for i in range(1, n + 1))

n = 1000
exact_value = riemann_zeta_10(n)
print(f"ζ(s) at s = 10 with n = {n}: {exact_value}")


# Add a space for a new paragraph
print("\n")  # This will create a blank line


text = 'Calculating the values of Riemann zeta function from s=1 to s=10 using Kummers Method'
print(text)
# Add a space for a new paragraph
print("\n")  # This will create a blank line

def alpha (p):
    """Calculates the value of alpha_p."""
    return 1 / (math.factorial(p) * p)

def kummer_improved_zeta(s, n=1000):
    """Calculates the Kummer-improved Riemann Zeta function for a given s."""
    if s <= 1:
        raise ValueError("Riemann Zeta function is not typically improved this way for s <=1 in this context.")

    alpha_s_minus_1 = alpha(s-1)
    sum_terms = 0
    for n in range(1, n + 1):
        term1 = 1 / (n ** s)
        denominator = 1
        for k in range(s):
            denominator*= (n + k)
        term2 = 1 / denominator
        sum_terms += (term1 - term2)
    
    return alpha_s_minus_1 +sum_terms

#Calculate and print the Kummer-improved zeta values
kummer_zeta_values = {}
print("Kummer-improved ζ(s) values")
for s in range(2,11):
    kummer_zeta = kummer_improved_zeta(s)
    kummer_zeta_values[s] = kummer_zeta
    print(f"Kummer-improved ζ({s}) ≈ {kummer_zeta}")