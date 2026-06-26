# main.py

import argparse
import os

from src.tsp import TSP
from src.heuristics import nearest_neighbor, cheapest_insertion
from src.vnd import vnd
from src.utils import ensure_dir, save_results, run_experiment, timestamp


def main():
   
    print("START")
   
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", type=str, required=True)
    parser.add_argument("--runs", type=int, default=5)

    args = parser.parse_args()

    print("STARTING EXPERIMENT...")

    # carregar instância
    tsp = TSP.from_tsplib(args.instance)
    instance_name = os.path.splitext(os.path.basename(args.instance))[0]

    # criar pasta
    ensure_dir("results")

    output_file = f"results/tsp_{instance_name}_{timestamp()}.csv"

    header = [
        "instance",
        "heuristic",
        "best_cost",
        "avg_cost",
        "avg_initial_cost",
        "avg_time",
        "runs",
        "best_solution"
    ]

    all_rows = []

    print("Running NN...")

    # ==========================
    # HEURÍSTICA 1
    # ==========================
    stats_nn = run_experiment(
        tsp,
        heuristic_func=nearest_neighbor,
        vnd_func=vnd,
        runs=args.runs,
        instance_name=instance_name
    )

    all_rows.append([
        stats_nn["instance"],
        stats_nn["heuristic"],
        stats_nn["best_cost"],
        stats_nn["avg_cost"],
        stats_nn["avg_initial_cost"],
        stats_nn["avg_time"],
        stats_nn["runs"],
        stats_nn["best_solution"]
    ])

    print("Running CI...")

    # ==========================
    # HEURÍSTICA 2
    # ==========================
    stats_ci = run_experiment(
        tsp,
        heuristic_func=cheapest_insertion,
        vnd_func=vnd,
        runs=args.runs,
        instance_name=instance_name
    )

    all_rows.append([
        stats_ci["instance"],
        stats_ci["heuristic"],
        stats_ci["best_cost"],
        stats_ci["avg_cost"],
        stats_ci["avg_initial_cost"],
        stats_ci["avg_time"],
        stats_ci["runs"],
        stats_ci["best_solution"]
    ])

    # salvar CSV
    for row in all_rows:
        save_results(output_file, header, row)

    # print resumo
    print("\n===== RESULTADOS =====")

    for row in all_rows:
        print(row)

    print(f"\nResultados salvos em: {output_file}")


if __name__ == "__main__":
    main()