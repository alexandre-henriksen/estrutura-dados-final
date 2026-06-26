# utils.py

import os
import csv
import time


def ensure_dir(path):
    """
    Garante que o diretório existe
    """
    os.makedirs(path, exist_ok=True)


def save_results(filepath, header, row):
    """
    Salva resultados em CSV (append)
    """
    file_exists = os.path.isfile(filepath)

    with open(filepath, mode='a', newline='') as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(header)

        writer.writerow(row)


def timestamp():
    """
    Retorna timestamp formatado
    """
    return time.strftime("%Y-%m-%d_%H-%M-%S")

'''
def run_experiment(tsp, heuristic_func, vnd_func, runs=5, instance_name="unknown"):
    """
    Executa múltiplas rodadas e retorna estatísticas completas.
    """

    results = []

    best_global_solution = None
    best_global_cost = float("inf")

    for i in range(runs):

        # solução inicial
        initial_solution = heuristic_func(tsp)
        initial_cost = tsp.route_cost(initial_solution)

        # VND
        best_solution, best_cost, exec_time = vnd_func(tsp, initial_solution)

        # salva resultados por execução
        results.append({
            "run": i,
            "initial_cost": initial_cost,
            "best_cost": best_cost,
            "time": exec_time,
            "initial_solution": initial_solution,
            "best_solution": best_solution
        })

        # guarda melhor global
        if best_cost < best_global_cost:
            best_global_cost = best_cost
            best_global_solution = best_solution

    # estatísticas agregadas
    avg_initial = sum(r["initial_cost"] for r in results) / runs
    avg_cost = sum(r["best_cost"] for r in results) / runs
    avg_time = sum(r["time"] for r in results) / runs

    return {
        "instance": instance_name,
        "runs": runs,

        # melhores resultados
        "best_cost": best_global_cost,
        "best_solution": best_global_solution,

        # médias
        "avg_initial_cost": avg_initial,
        "avg_cost": avg_cost,
        "avg_time": avg_time,

        # detalhamento completo
        "runs_detail": results
    }
'''

def run_experiment(tsp, heuristic_func, vnd_func, runs=5, instance_name="unknown"):
    """
    Executa múltiplas rodadas e retorna estatísticas completas.
    """

    results = []

    best_global_solution = None
    best_global_cost = float("inf")

    for i in range(runs):

        # solução inicial
        initial_solution = heuristic_func(tsp)
        initial_cost = tsp.route_cost(initial_solution)

        # VND
        best_solution, best_cost, exec_time = vnd_func(tsp, initial_solution)

        # salva resultados por execução
        results.append({
            "run": i,
            "initial_cost": initial_cost,
            "best_cost": best_cost,
            "time": exec_time,
            "initial_solution": initial_solution,
            "best_solution": best_solution
        })

        # guarda melhor global
        if best_cost < best_global_cost:
            best_global_cost = best_cost
            best_global_solution = best_solution

    # estatísticas agregadas
    avg_initial = sum(r["initial_cost"] for r in results) / runs
    avg_cost = sum(r["best_cost"] for r in results) / runs
    avg_time = sum(r["time"] for r in results) / runs

    return {
        "instance": instance_name,
        "heuristic": heuristic_func.__name__,
        "runs": runs,

        # melhores resultados
        "best_cost": best_global_cost,
        "best_solution": best_global_solution,

        # médias
        "avg_initial_cost": avg_initial,
        "avg_cost": avg_cost,
        "avg_time": avg_time,

        # detalhamento completo
        # "runs_detail": results
    }