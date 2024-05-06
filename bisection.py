def bisection_method(func, a, b, error_accept):
    """
    This function solves for an unknown root of a non-linear function given the function, the initial root boundaries,
    and an acceptable level of error.

    Parameters
    ----------
    func : str
        The user-defined function, which needs to be entered as a string.
    a : float
        The initial lower root boundary.
    b : float
        The initial upper root boundary.
    error_accept : float
        The user's acceptable level of error.

    Returns
    -------
    None
        Prints the root boundaries and the error at the final iteration.
    """

    def f(x):
        """
        Evaluates the function at a given value of x.

        Parameters
        ----------
        x : float
            The value of x at which to evaluate the function.

        Returns
        -------
        float
            The value of the function at x.
        """
        f = eval(func)
        return f

    error = abs(b - a)

    while error > error_accept:
        c = (b + a) / 2

        if f(a) * f(b) >= 0:
            print("No root or multiple roots present, therefore, the bisection method will not work!")
            return

        elif f(c) * f(a) < 0:
            b = c
            error = abs(b - a)

        elif f(c) * f(b) < 0:
            a = c
            error = abs(b - a)

        else:
            print("Something went wrong")
            return

    print(f"The error is {error}")
    print(f"The lower boundary, a, is {a} and the upper boundary, b, is {b}")


# Example usage of the bisection_method function
# change the equation to your desired equation to get your desired output.
bisection_method("(4*x**3)+3*x-3", 0, 1, 0.05)

bisection_method("(3*x**2)-4", -2, 0, 0.05)