#Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o
#preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais
#longas#

km = float(input("Informe quantos km vce deseja percorrer: "))
if km <= 200:
    valor = km*0.50
    print("O valor da passagem sera de: ", valor, "reais")

else:
    valor = km*0.45
    print("O valor da passagem sera de: ", valor,"reais")


