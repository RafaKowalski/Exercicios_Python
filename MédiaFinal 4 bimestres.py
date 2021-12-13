bim1n1 = float (input("digite a primera nota do primeiro bimestre: "))
bim1n2 = float (input("digite a segunda nota do primeiro bimestre: "))

nota1 = (bim1n1 + bim1n2)/2
print ("sua média do primeiro bimestre:{0:2.2f}" .format(nota1))

bim2n1 = float (input("digite a primeira nota do segundo bimestre: "))
bim2n2 = float (input("digite a segunda nota do segundo bimestre: "))

nota2 = (bim2n1 + bim2n2)/2
print ("sua média do segundo bimestre:{0:2.2f}" .format(nota2))

bim3n1 = float (input("digite a primeira nota do terceiro bimestre: "))
bim3n2 = float (input("digite a segunda nota do terceiro bimestre: "))

nota3 = (bim3n1 + bim3n2)/2
print ("sua média do primeiro bimestre:{0:2.2f}" .format(nota3))

bim4n1 = float (input("digite a primeira nota do quarto bimestre: "))
bim4n2 = float (input("digite a segunda nota do quarto bimestre: "))

nota4 = (bim4n1 + bim4n2)/2
print ("sua média do quarto bimestre:{0:2.2f}" .format(nota4))

medfinal = (nota1 + nota2 + nota3 + nota4)/4

print ("sua média final foi:{0:2.2f}" .format(medfinal))

if medfinal >= 7:
  print ("parabens voce foi aprovada barbara!")
else:
  print("reprovado")