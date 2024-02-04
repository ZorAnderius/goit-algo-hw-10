import numpy as np
import matplotlib.pyplot as plt
import random


from typing import Callable

from entry_data import boards, entry_func

def monte_carlo(func: Callable, boards: list, num_points: int, veiw: bool=False) -> float:
    x_min, x_max, y_min, y_max = boards[0], boards[1], boards[2], boards[3]
    x = np.random.uniform(x_min,x_max, num_points)
    y = np.random.uniform(y_min, y_max, num_points)
    
    inside_circle = y < func(x)
    under_curve = np.sum(y < func(x))
    area = (x_max - x_min) * (y_max - y_min) * (under_curve / num_points)
    if veiw:
        plt.figure(figsize=(8, 8))
        plt.scatter(x[inside_circle], y[inside_circle], color="blue", s=1)
        plt.scatter(x[~inside_circle], y[~inside_circle], color="red", s=1)
        plt.axis("equal")
        plt.show()
    return area

if __name__ == "__main__":
    num_points = 1_000_000
    print(monte_carlo(entry_func, boards, num_points))