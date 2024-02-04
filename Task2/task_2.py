from monte_carlo import monte_carlo
from scipy_func import scipy_integer

from entry_data import boards, entry_func, function_desc
from draw_plot import draw_plot

def task_2() -> None:
    draw_plot(entry_func, boards, function_desc)
    num_points_small = 1_000
    num_points_medium = 1_000_000
    num_points_large = 100_000_000
    res, error = scipy_integer(entry_func, boards)
    
    print(f'\nВизначення площі фігури утвореної функцією {function_desc} за використання:')
    print()
    print(f'   - бібліотеки SciPy                       - інтеграл = {res}, з точністю {error}')
    print()
    print(f'   - методу Монте-Карло (1_000 точок)       - інтеграл = {monte_carlo(entry_func, boards, num_points_small, True)}')
    print(f'   - методу Монте-Карло (1_000_000 точок)   - інтеграл = {monte_carlo(entry_func, boards, num_points_medium, True)}')
    print(f'   - методу Монте-Карло (100_000_000 точок) - інтеграл = {monte_carlo(entry_func, boards, num_points_large)}')
    print()

if __name__ == "__main__":
    task_2()
