# Definição de variáveis
# o input estava fora do exercício
nome = str(input("Digite seu primeiro nome: "))
sobrenome = str(input("Digite seu sobrenome: "))
idade = int(input("Digite sua idade: "))
ano_nascimento = int(2024 - idade)
altura_metros = float(input("Qual a sua altura: "))
maior_de_idade = idade >= 18

# Output
print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de Nascimento:', ano_nascimento)
print('É maior de idade?', maior_de_idade)
print('Altura em metros:', altura_metros)