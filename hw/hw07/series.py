def fibonacci(n):
    """
    Returns the nth Fibonacci number from the Fibonacci sequence.
    Example: fibonacci(0) == 0
             fibonacci(1) == 1
    """
    # Setup the starting conditions
    a = 0
    b = 1
    c = 0
    # check if its the first or second element in the sequence
    if n == 0:
        c = 0
    elif n == 1:
        c = 1
    else:
        # loop through the sequence adding the previous two numbers
        for i in range(n - 1):
            c = a + b
            a = b
            b = c

    return c


def lucas(n):
    """
    Returns the nth lucas number from the lucas sequence.
    Example: lucas(0) == 2
             lucas(1) == 1
    """
    a = 2
    b = 1
    c = 0
    if n == 0:
        c = 2
    elif n == 1:
        c = 1
    else:
        for i in range(n - 1):
            c = a + b
            a = b
            b = c

    return c


def sum_series(n, a=0, b=1):
    """
    Returns the nth sum inn a summation series that is dependent on the
    starting values passed when the fucntion is called (default = 0,1)
    """
    c = 0
    if n == 0:
        c = a
    elif n == 1:
        c = b
    else:
        for i in range(n - 1):
            c = a + b
            a = b
            b = c

    return c
