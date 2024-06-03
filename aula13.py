# formatação de strings

nome = str(input('Por favor, digite seu primeiro nome: '))
altura = int(input('Por favor, digite sua altura em centímetros: Ex 180 '))
peso = int(input('Por favor, digite seu peso: '))
imc = (peso / ((altura / 100) ** 2))

# Determinar o status de nutrição com base no IMC
if imc < 18.5:
    status = 'abaixo do peso'
elif 18.5 <= imc < 24.9:
    status = 'com peso normal'
elif 24.9 <= imc < 29.9:
    status = 'com sobrepeso'
elif 29.9 <= imc < 34.9:
    status = 'com obesidade grau I'
elif 34.9 <= imc < 39.9:
    status = 'com obesidade grau II (severa)'
else:
    status = 'com obesidade grau III (mórbida)'

linha_1 = f'{nome} tem {altura /100:.2f} de altura'
linha_2 = f'pesa, {peso}, quilos e seu IMC é {imc:.2f}'
linha_3 = f' e está {status}.'


print(linha_1)
print(linha_2)
print(linha_3)

# nome = 'Bertil'
# altura = se receber numero inteiro, dividir por 100 na exibição
# peso = 65

# Bertil tem 1.80 de altura, pesa 65 quilos e seu IMC é
# ... -> Elipsis / placeholder
