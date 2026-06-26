Problema do Caixeiro Viajante (TSP) com VND

****
=> Execute o algoritmo

python main.py --instance data/berlin52.tsp

python main.py --instance data/st70.tsp

python main.py --instance data/kroA100.tsp
****

Implementação do Problema do Caixeiro Viajante (TSP) utilizando metaheurísticas, com foco no algoritmo Variable Neighborhood Descent (VND).

Este projeto foi desenvolvido como parte da disciplina Estrutura de Dados e Complexidade de Algoritmos (Mestrado em Informática).

1. Descrição do Problema

O TSP consiste em encontrar a rota de menor custo que:

a) Visite todas as cidades exatamente uma vez
b) Retorne à cidade de origem

É um problema clássico de otimização combinatória e pertence à classe NP-completo.

2. Abordagem Utilizada

O projeto utiliza:

Heurística de construção inicial
Busca local com múltiplas vizinhanças
Metaheurística VND (Variable Neighborhood Descent)

3. Estrutura do Projeto

├── data/               # Instâncias do problema (TSPLIB)
├── docs/               # Documentação (enunciado do Projeto Final)
├── src/                # Código-fonte
│   ├── tsp.py          # Representação do problema
│   ├── heuristics.py   # Heurísticas de construção
│   ├── neighborhoods.py# Movimentos de vizinhança
│   ├── vnd.py          # Implementação do VND
│   └── utils.py        # Funções auxiliares
│
├── results/            # Resultados experimentais
├── main.py             # Pipeline de execução
├── tsp_step_by...iypnb # Notebook de análise e visualização
├── README.md
└── requirements.txt

4. Heurísticas Implementadas

* Construção inicial
Nearest Neighbor (Vizinho mais próximo)
Cheapest Insertion (Inserção mais barata)

* Vizinhanças
Swap (troca de cidades)
2-opt (remoção de cruzamentos)

5. Algoritmo VND

O VND explora múltiplas vizinhanças de forma sistemática:

Começa com uma solução inicial
Aplica uma vizinhança
Se houver melhoria → reinicia
Caso contrário → muda de vizinhança
Não havendo melhoria → finaliza

6. Como Executar

a) Clone o repositório
git clone https://github.com/alexandre-henriksen/tsp-vnd.git

b) Instale as dependências
pip install -r requirements.txt

c) Execute o algoritmo
python main.py --instance data/berlin52.tsp
python main.py --instance data/st70.tsp
python main.py --instance data/kroA100.tsp

7. Resultados

Exemplo de saída:

Instância	Melhor custo	Tempo (s)
berlin52	7749	0.19
st70	701	0.57
kroA100  21919   3.12

8. Instâncias Utilizadas

TSPLIB (biblioteca padrão de benchmark)
Exemplos:
berlin52
st70
kroA100

9. Autor

Alexandre Lauri Henriksen
