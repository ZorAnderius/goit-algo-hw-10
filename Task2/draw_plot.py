import matplotlib.pyplot as plt
import numpy as np

from typing import Callable


def draw_plot(entry_func: Callable, boards: list, function_desc: str='some function') -> None:
    # Створення діапазону значень для x
    x1, x2 = -4, 4
    x = np.linspace(x1, x2, 400)
    y = entry_func(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(boards[0], boards[1])
    iy = entry_func(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=boards[0], color='gray', linestyle='--')
    ax.axvline(x=boards[1], color='gray', linestyle='--')
    ax.set_title(f'Графік інтегрування {function_desc} від {x1}  до {x2}')
    plt.grid()
    plt.show()