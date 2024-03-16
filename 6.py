#6 -Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos.Utilize um bloco try-except para lidar com possíveis exceções.

Numeros_1_a_5=['1', '2', '3', '4', '5']
for i in Numeros_1_a_5:
  try:
    print(i)
  except:
    print('Erro', i)