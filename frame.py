n = int(input())

print('*' * (n + 2))
print(*['*' + (' ' * n) + '*' for i in range(n)], sep='\n')
print('*' * (n + 2))
