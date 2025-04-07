#Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto.
# Considere que pagam imposto pessoas cujo salário é maior que R$ 1.200,00.#

salario = float(input("Qual o seu salario?"))

if salario < 1200 :
    print("Voce nao deve pagar imposto")
else :
    print ("Voce deve pagar imposto")