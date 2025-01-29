from time import sleep  # Importa a função sleep para pausar a execução do programa

time = list()  # Lista para armazenar os dados de todos os jogadores
jogador = dict()  # Dicionário para armazenar os dados de um jogador

while True:  # Loop principal para cadastrar jogadores
    jogador.clear()  # Limpa o dicionário para um novo cadastro
    jogador['nome'] = str(input("Nome: "))  # Solicita o nome do jogador e armazena no dicionário
    partida = int(input(f"Quantas partidas o {jogador['nome']} jogou?: "))  # Solicita o número de partidas jogadas

    gol = list()  # Lista para armazenar os gols de cada partida
    soma = 0  # Variável para armazenar o total de gols
    for i in range(partida):  # Loop para coletar os gols de cada partida
        gols = int(input(f'Quantos gols na partida {i + 1}: '))  # Solicita os gols da partida atual
        soma += gols  # Adiciona os gols ao total
        gol.append(gols)  # Adiciona os gols da partida à lista de gols
    jogador["total"] = soma  # Armazena o total de gols no dicionário
    jogador["gol"] = gol[:]  # Armazena a lista de gols no dicionário do jogador
    time.append(jogador.copy())  # Adiciona uma cópia do dicionário do jogador à lista de jogadores

    r = ' '  # Variável para armazenar a resposta do usuário sobre continuar
    while r not in "SN":  # Loop para validar a resposta do usuário
        r = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]  # Solicita a resposta e formata
    if r == 'N':  # Se a resposta for 'N', encerra o loop principal
        break

# Exibe o cabeçalho da tabela de jogadores
print("=+=" * 30)
for i in jogador.keys():  # Loop para exibir as chaves do dicionário como cabeçalho
    print(f'{i:<23}', end=' ')  # Formata o cabeçalho para alinhar à esquerda
print()
print("=+=" * 30)

# Exibe os dados de todos os jogadores
for k, v in enumerate(time):  # Loop para percorrer a lista de jogadores
    print(f'{k:>5}', end=' ')  # Exibe o índice do jogador
    for d in v.values():  # Loop para exibir os valores do dicionário do jogador
        print(f"{str(d):<20}", end=' ')  # Formata os valores para alinhar à esquerda
    print()

# Loop para consultar os dados de um jogador específico
while True:
    busc = int(input('Mostrar qual jogador? (999 para sair): '))  # Solicita o índice do jogador
    if busc == 999:  # Se o usuário digitar 999, encerra o loop
        break
    elif busc >= len(time):  # Verifica se o índice é válido
        print('Erro! Jogador não encontrado.')
    else:
        # Exibe o levantamento de gols do jogador selecionado
        print(f">> LEVANTAMENTO DO {time[busc]['nome']}")
        for i, g in enumerate(time[busc]["gol"]):  # Loop para exibir os gols de cada partida
            print(f"    No jogo {i + 1} ele fez {g} gols.")