#7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

def calcular_media(lista):
    try:
        soma = sum(lista)
        media = soma / len(lista)
        return media
    except ZeroDivisionError:
        return "Erro: A lista está vazia. Não é possível calcular a média."

# Exemplo de uso
lista_valores = [10, 20, 30, 40, 50]
media = calcular_media(lista_valores)
print("Média dos valores na lista:", media)

lista_vazia = []
media_vazia = calcular_media(lista_vazia)
print("Média dos valores na lista vazia:", media_vazia)
