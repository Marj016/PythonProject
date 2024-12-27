import math

# Function to approximate the Riemann zeta function
def approximate_zeta(s, threshold=1e-10):
    """
    Approximates the Riemann zeta function using the series:
    zeta(s) = sum(1/n^s for n=1 to infinity)
    
    Args:
    - s: the input value for which zeta is to be computed.
    - threshold: the convergence threshold for the series.
    
    Returns:
    - Approximate value of zeta(s)
    - Number of terms (n) used in the approximation
    """
    sum_zeta = 0.0
    n = 1
    prev_sum = 0.0

    while True:
        sum_zeta += 1 / (n ** s)
        if abs(sum_zeta - prev_sum) < threshold:
            break
        prev_sum = sum_zeta
        n += 1

    return sum_zeta, n

# Known exact values for the Riemann zeta function at specific values of s
exact_values = {
    1: float('inf'),  # zeta(1) diverges
    2: math.pi**2 / 6,
    3: 1.2020569031595942,  # Apéry's constant
    4: math.pi**4 / 90,
    5: 1.036927755143444,
    6: math.pi**6 / 945,
    7: 1.0083492773819228,
    8: math.pi**8 / 9450,
    9: 1.001253812551254,
    10: math.pi**10 / 93555
}

# Function to print approximate values of zeta(s) and compare with exact values
def compute_and_compare_zeta():
    for s in range(1, 11):
        approx_zeta, terms_used = approximate_zeta(s)
        exact_zeta = exact_values.get(s, None)
        
        # Output the result
        print(f"Approximation of ζ({s}): {approx_zeta}")
        if exact_zeta is not None:
            print(f"Exact value of ζ({s}): {exact_zeta}")
            print(f"Difference: {abs(approx_zeta - exact_zeta)}")
        print(f"Number of terms used to reach convergence: {terms_used}\n")

# Run the function to compute and compare
# This is a comment that I will push to the repository
compute_and_compare_zeta()
