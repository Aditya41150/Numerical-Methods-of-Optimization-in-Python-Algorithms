def newtons_method(func, funcderiv, x, n):
    """
    Newton's method for finding roots of a function.
    
    Parameters:
    - func: The function whose root needs to be found.
    - funcderiv: The derivative of the function.
    - x: The initial guess for the root.
    - n: The number of iterations to perform.
    """
    
    def evaluate_function(x):
        """
        Evaluates the function at a given point x.
        """
        function = eval(func)
        return function
    
    def evaluate_derivative(x):
        """
        Evaluates the derivative of the function at a given point x.
        """
        derivative = eval(funcderiv)
        return derivative
    
    for iteration in range(1, n):
        new_guess = x - (evaluate_function(x) / evaluate_derivative(x))
        x = new_guess
    
    print(f"The root was found to be at {x} after {n} iterations")


# Example usage
newtons_method("x**2-2", "2*x", 2, 10)
newtons_method("x**2-2", "2*x", -10, 10)