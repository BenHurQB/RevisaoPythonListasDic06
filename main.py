#6) Escreva um programa que peça uma data informando o dia, mês e ano e determine se ela é uma data válida para uma análise.

def validarEntradaDeDados(data, testeData):
  if len(data) != 10 and data[2] != '/' and data[5] != '':
    print(f'\n{data} esta fora do escopo!!!\n')
  else:
    testeData = True
  return testeData
  
def verificarData(dia, mes, ano):
  valida = False
  if 0 < ano < 2100 and 1 <= mes <= 12:
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
      if 1 <= dia <= 31:
        valida = True
  if mes == 2:
    if ano % 4 == 0:
      if 1 <= dia <= 29:
        valida = True
    else: 
      if 1 <= dia <= 28:
        valida = True
  if mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if 1 <= dia <= 30:
      valida = True
      
  return valida    
  
def imprimirResultado(valida):
  
  if valida:
   print('\n\nData válida!!!\n') 
  else:
   print('\n\nData Inválida!!!\n')

#Entrada de dados


testeData = False
while testeData == False:
  data = input('Informe uma data: (XX / XX / XXXX) \n')
  testeData = validarEntradaDeDados(data, testeData)


#Declaração de variáveis

dia =int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:])

#Processar dados 
valida = verificarData(dia, mes, ano)
imprimirResultado(valida)