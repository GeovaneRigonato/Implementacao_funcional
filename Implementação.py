#Problema real: criar um programa que retorne o dobro de um número usando a função map.
def adicao(n): #declarar a função "adicao"
    return n + n
  
  
numeros = (1, 2, 3, 4)
resultado = map(adicao, numeros)
print(list(resultado))
