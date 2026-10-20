# Labirinto e algoritmos de busca

Este projeto representa um labirinto de 10 × 10 casas e compara três algoritmos para encontrar um caminho entre a entrada (`I`) e a saída (`F`). As paredes são marcadas com `#`, as casas livres com `.` e o caminho encontrado é mostrado com `*`.

## O labirinto

O mapa é definido diretamente no arquivo `lab.py`. Cada linha contém dez caracteres; o conjunto possui dez linhas. A entrada fica no canto superior esquerdo e a saída, no canto inferior direito. O movimento é permitido apenas para cima, para a direita, para baixo ou para a esquerda, sem atravessar paredes.

```text
I.........
...##.####
.##...###.
.##.......
..#..####.
.##....#..
.##.#.###.
..##....#.
.###....##
.........F
```

## Algoritmos

- **DFS (busca em profundidade):** explora um caminho até onde consegue e retorna para tentar outras opções quando encontra um beco sem saída. A ordem dos vizinhos influencia o caminho, que não precisa ser o mais curto.
- **BFS (busca em largura):** explora primeiro as casas mais próximas da entrada. Como cada movimento custa um passo, encontra um caminho com o menor número de passos.
- **Busca gulosa:** escolhe para explorar a casa que parece mais próxima da saída, usando a distância de Manhattan (diferença de linhas mais diferença de colunas). Essa estimativa não considera as paredes, então não garante o caminho mais curto.

Os algoritmos guardam o predecessor de cada casa descoberta para reconstruir o caminho depois de encontrar a saída. O programa imprime cada rota e uma tabela com os passos (movimentos entre casas) e as casas exploradas até alcançar a saída.

## Resultados

Resultados obtidos ao executar `python lab.py`:

| Algoritmo | Passos | Casas visitadas |
|---|---:|---:|
| DFS | 24 | 40 |
| BFS | 18 | 65 |
| Gulosa | 20 | 36 |

Neste mapa, a BFS encontrou a rota mais curta, com 18 passos. A DFS percorreu uma rota de 24 passos. A gulosa explorou menos casas que as outras duas, mas encontrou uma rota de 20 passos. A contagem de casas visitadas corresponde às posições retiradas para exploração; casas apenas descobertas e ainda não exploradas não entram na contagem.

## Como executar

Com Python 3 instalado, execute no terminal:

```bash
python lab.py
```
