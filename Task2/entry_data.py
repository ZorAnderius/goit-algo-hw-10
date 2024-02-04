from numpy import sin, ndarray
        # x_min, x_max, y_min, y_max
boards =  [-1,    1,     0,    5]

function_desc = 'f(x) = 5*sin(x^4) + x'
def entry_func(x: ndarray) -> ndarray:
    return 5 * sin(x**4) + x

