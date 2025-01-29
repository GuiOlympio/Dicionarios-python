# Importa a função randint para gerar números aleatórios
from random import randint

# Importa itemgetter para ordenar o dicionário com base nos valores
from operator import itemgetter

# Dicionário para armazenar os jogadores e seus resultados
jogo = {
    'jogador 1': randint(1, 6),
    'jogador 2': randint(1, 6),
    'jogador 3': randint(1, 6),
    'jogador 4': randint(1, 6)
}

# Exibe os resultados de cada jogador
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')

# Cria uma lista ordenada com base nos valores do dicionário (do maior para o menor)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

# Exibe o ranking dos jogadores
print("\n=== Ranking dos Jogadores ===")
for i, v in enumerate(ranking):
    print(f'{i + 1}° lugar: {v[0]} com {v[1]}')