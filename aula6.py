# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# # str, int, float, bool
# print(1+1) # 2
# print('a'+'b') #ab
# print('1'+1) # TypeError: can only concatenate str to str
print(int('1'), type(int('1'))) # <class 'int'>
print(float('1') + 1) # 2.0 decimal
print(type(float('1') + 1)) # <class 'float'>
print(bool(' ')) # True
print(str(11)+'b') # coerção -> 11b

