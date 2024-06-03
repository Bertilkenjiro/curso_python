# precedência de operadores

# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + - 
conta_1 = 1 + 1 ** 5 + 5 # 7
conta_1 = 1 ** 5 # 1 | a ultima coisa lida pelo interpretador
conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)

conta_2 = (1 + 1) ** (5 + 5) # 2 elevado a 10 | 1024
print(conta_2) 