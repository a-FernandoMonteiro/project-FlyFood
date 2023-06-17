#PROJETO INTERDISCIPLINAR PARA SISTEMAS DE INFORMAÇÃO II
#Aluno: Anderson Fernando Alves Monteiro da Silva - BSI

import itertools

def ler_arquivo():
    arquivo = open("matriz.txt" , "r")
    conteudoArquivo = arquivo.readlines()
    arquivo.close()
    return conteudoArquivo

def construir_lista_posicoes(conteudoArquivo):
    dimensoesMatriz = conteudoArquivo.pop(0).split()
    posicoesMatriz = []
    for linha in conteudoArquivo:
        posicoesMatriz.append(linha.strip().split())
    posicoesPontos = {} #pegando a letra e a posicao (linha, coluna) para o dic.
    linha, coluna = int(dimensoesMatriz[0]), int(dimensoesMatriz[1])
    for i in range(linha):
        for j in range(coluna):
            if posicoesMatriz[i][j] != "0":
                posicoesPontos[posicoesMatriz[i][j]] = (i,j)
    return posicoesMatriz, dimensoesMatriz, posicoesPontos

def construir_permutacoes(posicoesPontos, quantidadePontos):
    permutations = list(itertools.permutations(posicoesPontos, r = quantidadePontos))
    return permutations

def calcular_menor_caminho(todasPermutacoes, posicoesPontos, pontoR):
    distanciaMenorCaminho = float('inf')
    tuplaMenorCaminho = ()
    for permutacao in todasPermutacoes:
        caminhoPermutacao = 0
        primeiraPosicao = permutacao[0]
        xPrimeiraPosicao, yPrimeiraPosicao = posicoesPontos[primeiraPosicao]
        xR, yR = pontoR
        caminhoPrimeiroPonto = abs(xR - xPrimeiraPosicao) + abs(yR - yPrimeiraPosicao)
        for i in range(len(permutacao)-1):
            letra = permutacao[i]
            xLetra, yLetra = posicoesPontos[letra]
            proximaLetra = permutacao[i+1]
            xProximaLetra, yProximaLetra = posicoesPontos[proximaLetra]
            caminho = abs(xLetra - xProximaLetra) + abs(yLetra - yProximaLetra)
            caminhoPermutacao += caminho
        
        ultimaPosicao = len(permutacao)-1
        ultimaPosicao = permutacao[ultimaPosicao]
        xUltimaPosicao, yUltimaPosicao = posicoesPontos[ultimaPosicao]
        caminhoUltimoPonto = abs(xUltimaPosicao - xR) + abs(yUltimaPosicao - yR)
        custo = caminhoPrimeiroPonto + caminhoUltimoPonto
        caminhoPermutacao += custo

        if caminhoPermutacao < distanciaMenorCaminho:
            distanciaMenorCaminho = caminhoPermutacao
            tuplaMenorCaminho = permutacao
    return tuplaMenorCaminho, distanciaMenorCaminho

conteudoArquivo = ler_arquivo()
posicoesMatriz, dimensoesMatriz, posicoesPontos = construir_lista_posicoes(conteudoArquivo)
pontoR = posicoesPontos.pop("R")
todasPermutacoes = construir_permutacoes(posicoesPontos, len(posicoesPontos))
menorRota, menorDistancia = calcular_menor_caminho(todasPermutacoes, posicoesPontos, pontoR)

#RESULTADO
print("Menor caminho a ser percorrido: ",menorRota)
print("Distância a ser percorrida: %d dronômetros." %menorDistancia)