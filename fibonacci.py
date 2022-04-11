import math

#Função para verificar se um número inteiro tem raiz quadrada inteira
def is_square(integer):
    root = math.sqrt(integer)
    return integer == int(root + 0.5) ** 2

#Função para verificar se um número consta na sequência de fibonacci
def is_fibonacci(number):
  if is_square(5*number**2 + 4) or is_square(5*number**2 - 4):
    return True

#Solicitar usuário por input de dois números
x = int(input('Insira o primeiro número: '))
y = int(input('Insira o segundo número: '))

#Checar se os números constam na sequência
lista = []
if is_fibonacci(x) == True:
  if is_fibonacci(y) == True:
    #print('Ambos os valores fazem parte da sequência de Fibonacci')
    #Verificar números que constam na sequência que estejam no intervalo entre os valores do input do usuário (x e y)
    i = x
    while i <= y:
      if is_fibonacci(i):
        lista.append(i)
      i = i + 1
  else:
    print(f'O segundo número ({y}) não faz parte da sequência de Fibonacci')
else:
    print(f'O primeiro número ({x}) não faz parte da sequência de Fibonacci')

#Verificar condições especiais em que o primeiro número é 0 ou o primeiro número é 1, para que se garanta a aparição dos dois uns
if x == 0 and is_fibonacci(x):
  lista.insert(1, 1)
if x == 1 and is_fibonacci(x):
  lista.insert(1, 1)

if is_fibonacci(x) and is_fibonacci(y) == True:
    print(f'A sequência é a seguinte: {lista}')