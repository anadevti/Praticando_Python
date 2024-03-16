#5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

num = int(input('Digite um número: '))

for i in range(1, 11):
  print(f'{num} x {i} = {num*i}')
  print('O resultado é:', num*i)