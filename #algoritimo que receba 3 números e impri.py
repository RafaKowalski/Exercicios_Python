#algoritimo que receba 3 números e imprima condição satisfeita, somente se o primeiro número for maior do que os 2 últimos números, caso ao contrario, imprimir 'erro'

n1 = int(input("digite o primeiro numero: "))
n2 = int(input("digite o segundo numero: "))
n3 = int(input("digite o terceiro numero: "))

if n1 > n2 and n1 > n3:
    print("condição satisfeita",)
elif n1 == n2 and n1 == n3:
    print("numeros iguais, digite novamente")

else:
 print("error")

