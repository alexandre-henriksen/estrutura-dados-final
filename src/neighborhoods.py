# neighborhoods.py

def swap(route):
    """
    Gera melhor vizinho usando swap (troca de duas cidades)
    """
    best_route = route[:]
    n = len(route)

    for i in range(n - 1):
        for j in range(i + 1, n):
            new_route = route[:]
            new_route[i], new_route[j] = new_route[j], new_route[i]

            yield new_route


def two_opt(route):
    """
    Gera vizinhos usando movimento 2-opt
    """
    n = len(route)

    for i in range(n - 1):
        for j in range(i + 2, n):
            if i == 0 and j == n - 1:
                continue

            new_route = route[:]
            new_route[i + 1:j + 1] = reversed(new_route[i + 1:j + 1])

            yield new_route


def best_improvement(tsp, route, neighborhood_func):
    """
    Busca o melhor vizinho dentro de uma vizinhança
    """
    best = route
    best_cost = tsp.route_cost(route)

    for neighbor in neighborhood_func(route):
        cost = tsp.route_cost(neighbor)
        if cost < best_cost:
            best = neighbor
            best_cost = cost

    return best, best_cost