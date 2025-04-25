#Faça um programa que lê as duas notas parciais obtidas por um 
##aluno numa disciplina ao longo de um semestre, e 
#calcule a sua média. A atribuição de conceitos obedece à tabela 
##abaixo: 
#Média de Aproveitamento Conceito 
#➢ Entre 9.0 e 10.0 A 
#➢ Entre 7.5 e 9.0 B 
#➢ Entre 6.0 e 7.5 C 
#➢ Entre 4.0 e 6.0 D 
#➢ Entre 4.0 e zero E 
 
nota1 = float(input("Digite a primeira nota: ")) 
nota2 = float(input("Digite a segunda nota: ")) 
 
media = (nota1 + nota2) / 2 
 
if 9 <= media <= 10: 
   print(f"Sua media é: {media} e voce tirou um A") 
 
elif  7.5 <= media < 9: 
   print(f"Sua media é: {media} e voce tirou um B") 
 
elif  6 <= media < 7.5: 
   print(f"Sua media é: {media} e voce tirou um C") 
 
elif  4 <= media < 6: 
   print(f"Sua media é: {media} e voce tirou um D") 
 
elif  0 <= media < 4: 
   print(f"Sua media é: {media} e voce tirou um E") 
 
else: 
   print("média inválida")