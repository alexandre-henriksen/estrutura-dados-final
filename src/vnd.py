# vnd.py

import time
from .neighborhoods import swap, two_opt, best_improvement


def vnd(tsp, initial_solution, verbose=False):
    """
    Variable Neighborhood Descent (VND)

    Parameters:
    - tsp: instância do problema
    - initial_solution: solução inicial
    - verbose: imprime progresso

    Returns:
    - best_solution
    - best_cost
    - execution_time
    """

    neighborhoods = [swap, two_opt]

    current_solution = initial_solution
    current_cost = tsp.route_cost(current_solution)

    k = 0
    start_time = time.time()

    while k < len(neighborhoods):
        neighborhood = neighborhoods[k]

        new_solution, new_cost = best_improvement(
            tsp, current_solution, neighborhood
        )

        if new_cost < current_cost:
            current_solution = new_solution
            current_cost = new_cost
            k = 0  # reinicia
            if verbose:
                print(f"Improvement found: {current_cost}")
        else:
            k += 1

    end_time = time.time()

    return current_solution, current_cost, end_time - start_time



def vnd_move_choice(tsp, initial_solution, neighborhoods=None, verbose=False):
    """
    Variable Neighborhood Descent (VND) com escolha de movimentos.

    Parameters:
    - tsp: instância do problema
    - initial_solution: solução inicial (lista)
    - neighborhoods: lista de funções de vizinhança
    - verbose: imprime progresso

    Returns:
    - best_solution
    - best_cost
    - execution_time
    """

    # padrão se nada for passado
    if neighborhoods is None:
        neighborhoods = [swap, two_opt]

    current_solution = initial_solution
    current_cost = tsp.route_cost(current_solution)

    k = 0
    start_time = time.time()

    while k < len(neighborhoods):

        neighborhood_func = neighborhoods[k]

        new_solution, new_cost = best_improvement(
            tsp,
            current_solution,
            neighborhood_func
        )

        if new_cost < current_cost:
            current_solution = new_solution
            current_cost = new_cost
            k = 0  # reinicia sequência

            if verbose:
                print(f"[{neighborhood_func.__name__}] improvement: {current_cost}")

        else:
            k += 1

    end_time = time.time()

    return current_solution, current_cost, end_time - start_time