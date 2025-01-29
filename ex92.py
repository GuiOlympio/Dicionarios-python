# Importa a classe datetime para trabalhar com datas
from datetime import datetime

# Dicionário para armazenar os dados da pessoa
dado = {}

# Solicita o nome da pessoa e armazena no dicionário
dado['nome'] = str(input("Nome: "))

# Solicita o ano de nascimento e calcula a idade
nasc = int(input("Ano de nascimento: "))
dado["idade"] = datetime.now().year - nasc

# Solicita o número da carteira de trabalho (CTPS)
dado['ctps'] = int(input("Carteira de trabalho (0 se não tiver): "))

# Se a pessoa tiver CTPS, solicita informações adicionais
if dado['ctps'] != 0:
    dado['contratacao'] = int(input("Ano de contratação: "))
    dado['salario'] = float(input("Salário: R$ "))

    # Calcula a idade de aposentadoria
    # Aposentadoria = idade atual + (35 anos de contribuição - anos já trabalhados)
    anos_trabalhados = datetime.now().year - dado['contratacao']
    dado['aposentadoria'] = dado['idade'] + (35 - anos_trabalhados)

# Exibe uma linha de separação
print("=-=-" * 15)

# Exibe todos os dados armazenados no dicionário
for k, v in dado.items():
    print(f'{k} tem o valor {v}')