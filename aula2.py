# afuncao print serve para mostrar coisas na tela.
# podem ser varios argumentos

print(12, 34) #argumentos nao nomeados
print(56, 78) #por padrao possuem espacos e quebras de linha

print(12, 34, sep='-') 
print(56, 78, sep='-') 

# existem caracteres que por padrao nao aparecem
# mas que estao executando acoes 
# \r = return \n = line feed (quebra de linha)

print(1, 2, sep='-', end='\r\n') # sistemas windows | argumentos nomeados
print(3, 4, sep='-', end='\n') # sistemas Unix | argumentos nomeados


