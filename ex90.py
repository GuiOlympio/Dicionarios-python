# Dicionário para armazenar a situação do aluno
situacao = dict()

# Lista para armazenar o boletim (caso queira expandir o código no futuro)
boletim = list()

# Solicita o nome do aluno e armazena no dicionário
situacao["nome"] = str(input("Nome: "))

# Solicita a média do aluno e armazena no dicionário
situacao["media"] = float(input(f"Sua média de {situacao['nome']} foi? "))

# Exibe os dados do dicionário (nome e média)
for k, v in situacao.items():
    print(f'{k} é igual a {v}')

# Verifica se o aluno foi aprovado ou reprovado
if situacao["media"] >= 7:
    print('Aluno aprovado!')
else:
    print('Aluno reprovado!')

