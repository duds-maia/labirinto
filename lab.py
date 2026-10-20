#A atividade deverá ser disponibilizada em um repositório no GitHub, contendo:

#Implementação de um labirinto próprio, com dimensão mínima de 10 × 10.
#Implementação dos algoritmos DFS, BFS e Busca Gulosa, retornando o caminho encontrado e o número de casas visitadas.
#Visualização dos três caminhos no labirinto.
#Tabela comparativa com o tamanho do caminho e a quantidade de casas visitadas por algoritmo.
#Arquivo README.md com uma breve explicação do labirinto desenvolvido, das implementações e dos resultados obtidos.
from collections import deque
import heapq

labirinto = [
    "I.........",
    "...##.####",
    ".##...###.",
    ".##.......",
    "..#..####.",
    ".##....#..",
    ".##.#.###.",
    "..##....#.",
    ".###....##",
    ".........F",
]

DIRECOES = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def achar(lab, simbolo):
    for i, linha in enumerate(lab):
        if simbolo in linha:
            return (i, linha.index(simbolo))


def livre(lab, i, j):
    dentro = 0 <= i < len(lab) and 0 <= j < len(lab[0])
    return dentro and lab[i][j] != '#'

def montar_grafo(lab):
    grafo = {}
    for i in range(len(lab)):
        for j in range(len(lab[0])):
            if not livre(lab, i, j):
                continue
            grafo[(i, j)] = []
            for di, dj in DIRECOES:
                if livre(lab, i + di, j + dj):
                    grafo[(i, j)].append((i + di, j + dj))
    return grafo

def desenhar(lab, caminho):
    grade = [list(linha) for linha in lab]
    for i, j in caminho:
        if grade[i][j] == '.':
            grade[i][j] = '*'
    for linha in grade:
        print(''.join(linha))


def reconstruir(pais, saida):
    caminho = []
    atual = saida
    while atual is not None:
        caminho.append(atual)
        atual = pais[atual]
    caminho.reverse()
    return caminho


def dfs(grafo, inicio, saida):
    pais = {inicio: None}
    casas_visitadas = []

    def visitar(v):
        casas_visitadas.append(v)
        if v == saida:
            return True
        for w in grafo[v]:
            if w not in pais:
                pais[w] = v
                if visitar(w):
                    return True
        return False

    if visitar(inicio):
        return reconstruir(pais, saida), casas_visitadas
    return [], casas_visitadas

def bfs(grafo, inicio, saida):
    fila = deque([inicio])
    pais = {inicio: None}
    casas_visitadas = []
    while fila:
        v = fila.popleft()
        casas_visitadas.append(v)
        if v == saida:
            return reconstruir(pais, saida), casas_visitadas
        for w in grafo[v]:
            if w not in pais:

                pais[w] = v
                fila.append(w)
    return [], casas_visitadas

def h(v, saida):
    return abs(v[0] - saida[0]) + abs(v[1] - saida[1])

def gulosa(grafo, inicio, saida):
    fronteira = [(h(inicio, saida), inicio)]
    pais = {inicio: None}
    casas_visitadas = []
    while fronteira:
        _, v = heapq.heappop(fronteira)
        casas_visitadas.append(v)
        if v == saida:
            return reconstruir(pais, saida), casas_visitadas
        for w in grafo[v]:
            if w not in pais:
                pais[w] = v
                heapq.heappush(fronteira, (h(w, saida), w))
    return [], casas_visitadas

def main():
    grafo = montar_grafo(labirinto)
    inicio = achar(labirinto, 'I')
    saida = achar(labirinto, 'F')
    print('I = entrada | F = saida | # = parede | . = livre | * = caminho')
    resultados = []
    for nome, busca in [('DFS', dfs), ('BFS', bfs), ('Gulosa', gulosa)]:
        caminho, visitadas = busca(grafo, inicio, saida)
        resultados.append((nome, len(caminho) - 1 if caminho else '-',
                           len(visitadas)))
        print('\n' + nome + ':')
        desenhar(labirinto, caminho)

    print('\nCOMPARACAO')
    print(f'{"Busca":<10} {"Passos":>8} {"Casas visitadas":>18}')
    for nome, passos, visitas in resultados:
        print(f'{nome:<10} {str(passos):>8} {visitas:>18}')

if __name__ == '__main__':
    main()
