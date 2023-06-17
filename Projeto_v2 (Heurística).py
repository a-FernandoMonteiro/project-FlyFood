#PROJETO INTERDISCIPLINAR PARA SISTEMAS DE INFORMAÇÃO II
#Aluno: Anderson Fernando Alves Monteiro da Silva - BSI

def ler_arquivo():
    arquivo = open("matriz.txt", "r")
    matriz = arquivo.readlines()
    arquivo.close()
    return matriz

def construir_lista_posicoes(matriz):
    dimensoesMatriz = matriz.pop(0).split()
    listaMatriz = [] 
    posicoesPontos = {} 
    
    for pontosEntrega in matriz:
        listaMatriz.append(pontosEntrega.strip().split())
    
    x, y = int(dimensoesMatriz[0]), int(dimensoesMatriz[1]) 

    for i in range(x): #PEGAR PONTO DE ENTREGA E SUA POSIÇÃO P/ DICT => ex {"D":1,2}
        for j in range(y):
            if listaMatriz[i][j] != "0":
                posicoesPontos[listaMatriz[i][j]] = (i,j) 
    return dimensoesMatriz, listaMatriz, posicoesPontos

def calcular_distancias(posicoesPontos):
    pontoInicial_R = posicoesPontos.pop('R')  
    xInicial, yInicial = pontoInicial_R
    xFinalR, yFinalR = pontoInicial_R
    
    melhorCustoRota = float("inf")
    removerPonto = ''
    melhorRota = ''
    dronometros = 0
    
    for i in range(len(posicoesPontos)):
        melhorCustoRota = float("inf")
        
        for j in posicoesPontos: #PERCORRER AS LETRAS E PEGANDO SUA POSICAO PARA REALIZAR O CALCULO
            xPonto, yPonto = posicoesPontos[j]
            custoAtual = abs(xInicial - xPonto) + abs(yInicial - yPonto)
            
            if melhorCustoRota > custoAtual:
                melhorCustoRota = custoAtual
                removerPonto = j
            
            else:
                melhorCustoRota = melhorCustoRota
        
        melhorRota += removerPonto
        xInicial, yInicial = posicoesPontos[removerPonto] # SAINDO DO LAÇO VAI SE TORNAR O ULTIMO PONTO       
        dronometros += melhorCustoRota
        posicoesPontos.pop(removerPonto)
    
    custoFinal = abs(xFinalR - xInicial) + abs(yFinalR - yInicial)
    dronometros += custoFinal
    
    melhorRota = "R" + melhorRota + "R"
    
    return dronometros, melhorRota
        
matriz = ler_arquivo()
dimensoesMatriz, listaMatriz, posicoesPontos = construir_lista_posicoes(matriz)
dronometros, melhorRota= calcular_distancias(posicoesPontos)

#RESULTADO
print("Menor caminho a ser percorrido: ",melhorRota)
print("Distância a ser percorrida: %d dronômetros." %dronometros)