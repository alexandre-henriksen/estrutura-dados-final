# tsp.py

import math


class TSP:
    def __init__(self, coordinates=None, distance_matrix=None):
        """
        Inicializa o problema TSP.

        Parameters:
        - coordinates: lista de tuplas (x, y)
        - distance_matrix: matriz de distâncias pré-computada
        """
        if coordinates is None and distance_matrix is None:
            raise ValueError("Forneça coordenadas ou matriz de distâncias.")

        self.coordinates = coordinates
        self.n = len(coordinates) if coordinates else len(distance_matrix)

        if distance_matrix:
            self.dist_matrix = distance_matrix
        else:
            self.dist_matrix = self._compute_distance_matrix()

    def _euclidean_distance(self, i, j):
        """Distância euclidiana entre dois pontos"""
        x1, y1 = self.coordinates[i]
        x2, y2 = self.coordinates[j]
        return int(round(math.hypot(x1 - x2, y1 - y2)))
        #return math.hypot(x1 - x2, y1 - y2) --- TSPLIB usa arredondamento para inteiro

    def _compute_distance_matrix(self):
        """Gera matriz de distâncias"""
        dist = [[0] * self.n for _ in range(self.n)]

        for i in range(self.n):
            for j in range(self.n):
                if i != j:
                    dist[i][j] = self._euclidean_distance(i, j)

        return dist

    def distance(self, i, j):
        """Retorna distância entre i e j"""
        return self.dist_matrix[i][j]

    def route_cost(self, route):
        """
        Calcula custo total da rota (ciclo fechado)
        route: lista de cidades
        """
        cost = 0
        n = len(route)

        for i in range(n):
            cost += self.distance(route[i], route[(i + 1) % n]) # n mod n = 0: última cidade → primeira cidade

        return cost

    def is_valid_route(self, route):
        """Verifica se rota é válida"""
        return set(route) == set(range(self.n)) and len(route) == self.n

    @staticmethod
    def from_tsplib(file_path):
        """
        Lê arquivo TSPLIB (formato EUC_2D)
        """
        coordinates = []

        with open(file_path, 'r') as f:
            reading_coords = False
            for line in f:
                line = line.strip()

                if line.startswith("NODE_COORD_SECTION"):
                    reading_coords = True
                    continue

                if line.startswith("EOF"):
                    break

                if reading_coords:
                    parts = line.split()
                    _, x, y = parts
                    coordinates.append((float(x), float(y)))

        return TSP(coordinates=coordinates)