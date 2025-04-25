#Faça um Programa que, tendo como dados de entrada o preço de 
##custo de um produto e um código de origem, emita o 
#preço junto de sua procedência. Caso o código não seja nenhum dos 
##especificados, o produto deve ser classificado 
#como importado. 
#Código de origem: 1 - Sul, 2 - Norte 3 - Leste, 4 - Oeste, 5 ou 6 - nordeste 7 ou 8 Centro-oeste. 
 
preco = float(input( "Digite o preço de custo do produto: ")) 
codigo = int(input("Digite o código de origem do produto: ")) 
 
if codigo == 1: 
   procedencia = "Sul" 
elif  codigo == 2: 
   procedencia = "Norte" 
 
elif  codigo == 3: 
   procedencia = "Leste" 
 
elif  codigo == 4: 
   procedencia = "Oeste" 
 
elif  codigo == 5: 
   procedencia = "Nordeste" 
 
elif  codigo == 6: 
   procedencia = "Centro oeste" 
 
else: 
   procedencia = "Importado" 
 
 
print(f"Preço e procedência: {preco}, {procedencia}") 