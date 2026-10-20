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

def achar(mapa, simbolo):
    for indice_linha, linha in enumerate(mapa):
        if simbolo in linha:
            return (indice_linha, linha.index(simbolo))


def livre(mapa, indice_linha, indice_coluna):
    dentro_do_mapa = 0 <= indice_linha < len(mapa) and 0 <= indice_coluna < len(mapa[0])
    return dentro_do_mapa and mapa[indice_linha][indice_coluna] != '#'

def montar_grafo(mapa):
    grafo = {}
    for indice_linha in range(len(mapa)):
        for indice_coluna in range(len(mapa[0])):
            if not livre(mapa, indice_linha, indice_coluna):
                continue
            grafo[(indice_linha, indice_coluna)] = []
            for movimento_linha, movimento_coluna in DIRECOES:
                if livre(mapa, indice_linha + movimento_linha, indice_coluna + movimento_coluna):
                    grafo[(indice_linha, indice_coluna)].append((indice_linha + movimento_linha, indice_coluna + movimento_coluna))
    return grafo

def desenhar(mapa, caminho):
    mapa_desenhado = [list(linha) for linha in mapa]
    for indice_linha, indice_coluna in caminho:
        if mapa_desenhado[indice_linha][indice_coluna] == '.':
            mapa_desenhado[indice_linha][indice_coluna] = '*'
    for linha in mapa_desenhado:
        print(''.join(linha))


def reconstruir(antecessores, saida):
    caminho = []
    casa_atual = saida
    while casa_atual is not None:
        caminho.append(casa_atual)
        casa_atual = antecessores[casa_atual]
    caminho.reverse()
    return caminho


def dfs(grafo, inicio, saida):
    antecessores = {inicio: None}
    casas_visitadas = []

    def visitar(casa_atual):
        casas_visitadas.append(casa_atual)
        if casa_atual == saida:
            return True
        for casa_vizinha in grafo[casa_atual]:
            if casa_vizinha not in antecessores:
                antecessores[casa_vizinha] = casa_atual
                if visitar(casa_vizinha):
                    return True
        return False

    if visitar(inicio):
        return reconstruir(antecessores, saida), casas_visitadas
    return [], casas_visitadas

def bfs(grafo, inicio, saida):
    fila = [inicio]
    indice_fila = 0
    antecessores = {inicio: None}
    casas_visitadas = []
    while indice_fila < len(fila):
        casa_atual = fila[indice_fila]
        indice_fila += 1
        casas_visitadas.append(casa_atual)
        if casa_atual == saida:
            return reconstruir(antecessores, saida), casas_visitadas
        for casa_vizinha in grafo[casa_atual]:
            if casa_vizinha not in antecessores:

                antecessores[casa_vizinha] = casa_atual
                fila.append(casa_vizinha)
    return [], casas_visitadas

def h(casa_atual, saida):
    return abs(casa_atual[0] - saida[0]) + abs(casa_atual[1] - saida[1])

def gulosa(grafo, inicio, saida):
    fronteira = [(h(inicio, saida), inicio)]
    antecessores = {inicio: None}
    casas_visitadas = []
    while fronteira:

        melhor_opcao = min(fronteira)
        fronteira.remove(melhor_opcao)
        _, casa_atual = melhor_opcao
        casas_visitadas.append(casa_atual)
        if casa_atual == saida:
            return reconstruir(antecessores, saida), casas_visitadas
        for casa_vizinha in grafo[casa_atual]:
            if casa_vizinha not in antecessores:
                antecessores[casa_vizinha] = casa_atual
                fronteira.append((h(casa_vizinha, saida), casa_vizinha))
    return [], casas_visitadas

def main():
    grafo = montar_grafo(labirinto)
    inicio = achar(labirinto, 'I')
    saida = achar(labirinto, 'F')
    print('I = entrada | F = saida | # = parede | . = livre | * = caminho')
    resultados = []
    for nome_busca, algoritmo in [('DFS', dfs), ('BFS', bfs), ('Gulosa', gulosa)]:
        caminho, visitadas = algoritmo(grafo, inicio, saida)
        resultados.append((nome_busca, len(caminho) - 1 if caminho else '-',
                           len(visitadas)))
        print('\n' + nome_busca + ':')
        desenhar(labirinto, caminho)

    print('\nCOMPARACAO')
    print(f'{"Busca":<10} {"Passos":>8} {"Casas visitadas":>18}')
    for nome_busca, passos, visitas in resultados:
        print(f'{nome_busca:<10} {str(passos):>8} {visitas:>18}')

if __name__ == '__main__':
    main()
