# heuristics.py

import random


def nearest_neighbor(tsp, start=0):
    """
    Heurística do vizinho mais próximo.

    Parameters:
    - tsp: instância da classe TSP
    - start: cidade inicial

    Returns:
    - rota (lista de índices)
    """
    n = tsp.n
    unvisited = set(range(n))
    route = [start]
    unvisited.remove(start)

    current = start

    while unvisited:
        next_city = min(unvisited, key=lambda city: tsp.distance(current, city))
        route.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    return route


def nearest_neighbor_randomized(tsp, alpha=0.3):
    """
    Versão randomizada do nearest neighbor (GRASP-like).

    alpha controla o nível de aleatoriedade.
    """
    n = tsp.n
    start = random.randint(0, n - 1)

    unvisited = set(range(n))
    route = [start]
    unvisited.remove(start)

    current = start

    while unvisited:
        distances = [(city, tsp.distance(current, city)) for city in unvisited]
        distances.sort(key=lambda x: x[1])

        # Lista restrita de candidatos (RCL)
        k = max(1, int(len(distances) * alpha))
        rcl = distances[:k]

        next_city = random.choice(rcl)[0]

        route.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    return route


def cheapest_insertion(tsp, initial_route=None):
    """
    Heurística de inserção mais barata.
    """
    n = tsp.n

    # começa com 2 nós

    if initial_route is None:
        initial_route = [0, 1]

    route = list(initial_route)
    unvisited = set(range(n)) - set(route)

    while unvisited:
        best_increase = float('inf')
        best_city = None
        best_position = None

        for city in unvisited:
            for i in range(len(route)):
                j = (i + 1) % len(route)

                cost_increase = (
                    tsp.distance(route[i], city)
                    + tsp.distance(city, route[j])
                    - tsp.distance(route[i], route[j])
                )

                if cost_increase < best_increase:
                    best_increase = cost_increase
                    best_city = city
                    best_position = j

        route.insert(best_position, best_city)
        unvisited.remove(best_city)

    return route


def random_solution(tsp):
    """
    Gera solução aleatória válida.
    """
    route = list(range(tsp.n))
    random.shuffle(route)
    return route