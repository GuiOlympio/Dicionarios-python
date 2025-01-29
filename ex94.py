# Lista para armazenar todas as pessoas cadastradas
galera = list()

# Dicionário para armazenar os dados de uma pessoa
pessoa = dict()

# Variáveis para calcular a soma das idades e a média
soma = media = 0

# Loop principal para cadastrar pessoas
while True:
    # Limpa o dicionário para um novo cadastro
    pessoa.clear()

    # Solicita o nome da pessoa
    pessoa["nome"] = str(input("Nome: "))

    # Loop para validar o sexo (apenas 'F' ou 'M')
    while True:
        pessoa["sexo"] = str(input("Sexo [F/M]: ")).strip().upper()[0]
        if pessoa["sexo"] in 'FM':
            break
        else:
            print("[ERRO!] Digite apenas F ou M.")

    # Solicita a idade da pessoa e adiciona à soma total
    pessoa["idade"] = int(input("Idade: "))
    soma += pessoa["idade"]

    # Adiciona uma cópia do dicionário da pessoa à lista 'galera'
    galera.append(pessoa.copy())

    # Loop para validar se o usuário deseja continuar cadastrando
    while True:
        r = str(input("Continuar? [S/N] ")).strip().upper()[0]
        if r in 'SN':
            break
        else:
            print("[ERRO!] Digite apenas S ou N.")

    # Se a resposta for 'N', encerra o loop principal
    if r == "N":
        break

# Calcula a média de idade
media = soma / len(galera)

# Exibe o total de pessoas cadastradas
print(f"Ao todo temos {len(galera)} pessoas cadastradas.")

# Exibe a média de idade com duas casas decimais
print(f"A média de idade é {media:.2f} anos.")

# Exibe todas as mulheres cadastradas
print("Todas as mulheres cadastradas foram: ", end="")
for p in galera:
    if p["sexo"] == 'F':
        print(f'{p["nome"]}', end=" ")
print()  # Pula uma linha após a lista de mulheres

# Exibe as pessoas com idade acima da média
print("Lista de pessoas com idade acima da média: ")
for p in galera:
    if p["idade"] >= media:
        for k, v in p.items():
            print(f'{k} = {v}', end="; ")  # Exibe cada campo do dicionário
        print()  # Pula uma linha após cada pessoa