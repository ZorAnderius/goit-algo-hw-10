import pulp

def task_1() -> None:
    model = pulp.LpProblem('Maximize_production', pulp.LpMaximize)

    lemonade = pulp.LpVariable('lemonade', lowBound=0, cat='Integer')
    fruit_juice = pulp.LpVariable('Fruit_juice', lowBound=0, cat='Integer')

    # target function
    model += lemonade + fruit_juice, 'The_total_number_of_manufactured_products'
    
    model += 2 * lemonade + fruit_juice <= 100, 'Water'
    model += lemonade <= 50, 'Sugar'
    model += lemonade <= 30, 'Lemon_juice'
    model += 2 * fruit_juice <= 40, 'Mashed_fruit'
    
    
    solver = pulp.PULP_CBC_CMD(msg=False)
    model.solve(solver)
    
    print('\nДля максимізації виробництва необхідно виробляти: ')
    print(f'   - ламонад:       {int(lemonade.varValue)} шт.')    
    print(f'   - фруковий сік : {int(fruit_juice.varValue)} шт.')    
    print()

if __name__ == "__main__":
    task_1()
