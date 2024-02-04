import scipy.integrate as spi

from typing import Callable

from entry_data import boards, entry_func

# Обчислення інтеграла
def scipy_integer(entry_func: Callable, boards: list) -> float:
    x_min, x_max = boards[0], boards[1]
    return spi.quad(entry_func, x_min, x_max)

if __name__ == '__main__':
    print(scipy_integer(entry_func, boards))