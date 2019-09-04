#ATIVIDADE PEDIDA: (Prof.Ronaldo)####################################################################################################################################################
#CT0110 – Décima contribuição da primeira etapa                                                                                                                                     #
#Implementar o Heap sort e imprimir os graficos conforme segue:                                                                                                                     #
#                                                                                                                                                                                   #
#   *Tamanho da lista de números x Tempo para ordenar pelo método - OBRIGATÓRIO!                                                                                                    #
#   [Tamanho da lista x Quantidade de operações (Número de comparações)] - OPCIONAL!                                                                                                #
#                                                                                                                                                                                   #
#As listas geradas devem ser de números aleatórios dos seguintes tamanhos: 100K, 200K, 400K, 500K, 1M, 2M.                                                                          #
#####################################################################################################################################################################################

#"Importação das devidas bibliotecas ;)"

import sys

import math

import random
from random import randint

import timeit

import numpy as np

import matplotlib as mpl

import matplotlib.pyplot as plt

###############################################################################{
#"Declarações iniciais..."
mpl.use('Agg')
mpl.rc('axes', linewidth=5)
plt.style.use('fast')
sys.setrecursionlimit(10**9)
###############################################################################}         

#"Segunda Função responsável pela criação do gráfico(x,y) para estudo do desempenho de algoritmo" *(Usada para criar o gráfico dos 3 casos apresentados juntos na mesma malha)
#Implementação do professor + implementação do aluno####################################################################################################{      
def desenhaGrafico2(x, y, yde, yce, file_name, label, label2, label3, file_title, line_color, line_color2, line_color3, xl, yl):                                                                                               #
    fig = plt.figure(figsize=(20, 20))                                                                                                                                                                 
    ax = fig.add_subplot(111)                                                                                                                          
    ax.plot(x,y, color=line_color,linestyle = '-.',linewidth=3,label = label)                           
    ax.plot(x,yde, color=line_color2,linestyle = '--',linewidth=2,label = label2)                     
    ax.plot(x,yce, color=line_color3,linestyle = '-',linewidth=1,label = label3)
                                                                     
    stemlines = plt.stem(x,y, markerfmt=' ',linefmt='k:', basefmt=' ',use_line_collection=True)                                                                                                 
    plt.setp(stemlines, 'linewidth', 1)                                                                                                                
    stemlines = plt.stem(x,yde, markerfmt=' ',linefmt='k:', basefmt=' ',use_line_collection=True)                                                                                            
    plt.setp(stemlines, 'linewidth', 1)                                                                                                                
    stemlines = plt.stem(x,yce, markerfmt=' ',linefmt='k:', basefmt=' ',use_line_collection=True)                                                                                                
    plt.setp(stemlines, 'linewidth', 1)

    plt.scatter(x[5],y[5], s=800,marker='^',facecolor='none',edgecolors= line_color, linewidths=1)
    plt.scatter(x[5],yde[5], s=800,marker='o',facecolor='none',edgecolors= line_color2, linewidths=1)
    plt.scatter(x[5],yce[5], s=800,marker='s',facecolor='none',edgecolors= line_color3, linewidths=1)
                                                                                                                                                                                                                                                                                            
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)                                                                              
    plt.ylabel(yl)                                                                                                                                                                                                                         
    plt.xlabel(xl)                                                                                                                                                                                                                         
    plt.title(file_title)                                                                                                                                                                                                            
    fig.savefig(file_name)                                                                                                                                                                                                          
########################################################################################################################################################}       

num_iteracoes = 0#<-Variável GLOBAL para se contar os 'SWAPS'

#"Função De Ordenação Auxiliar do Heap Sort"
#Implementação do aluno#########################################################################{
# variável 'n' é o tamanho do 'heap' 
def heapify(arr, n, i):

    global num_iteracoes
    
    largest = i  # inicializa a variável 'largest' como nossa raíz('root'): 
    l = 2 * i + 1     # (ramo)esquerda = 2*i + 1 
    r = 2 * i + 2     # (ramo)direita = 2*i + 2 
  
    # Verifica se o filho(ramificação) esquerdo da raíz escolhida EXISTE e é 
    # maior que a raíz: 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # Verifica se o filho(ramificação) direito da raíz escolhida EXISTE e é 
    # maior que a raíz: 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Mudamos a 'root', se necessário: 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  # Swap
        num_iteracoes += 1
  
        # 'Heapify' a 'root': 
        heapify(arr, n, largest) 
################################################################################################}

#"Função Heap Sort"
#Implementação do aluno#########################################################################{
def heapSort(lista):                                                                                                                                                                                                                            
    n = len(lista) 

    global num_iteracoes
  
    # Construímos um "heap máximo(maxheap)". 
    for i in range(n, -1, -1): 
        heapify(lista, n, i) 
  
    # Depois, de um por um, extraímos os elementos 
    for i in range(n-1, 0, -1): 
        lista[i], lista[0] = lista[0], lista[i]   # Swap
        num_iteracoes += 1
        heapify(lista, i, 0)

    aux = num_iteracoes 

    return aux
################################################################################################}

#"Função que ordena um número determinado(em função da entrada) de valores gerados aleatoriamente ou em certa ordem específica(Para essa NONA ATIVIDADE será em ordem ALEATÓRIA) e retorna os devidos gráficos comparativos"
#Obs.:(O que estiver comentado no código da função abaixo foi usado para gerar os outros gráficos)
#Implementação do aluno##########################################################################################################################################################################################################################################################################################################################################{
def cria_Graficos(lista_entrada):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   #

  global num_iteracoes

  tempos_orden_Random = list()
  tempos_orden_Decresc = list()   
  tempos_orden_Cresc = list()

  num_iteracoes_Random = list()
  num_iteracoes_Decresc = list()   
  num_iteracoes_Cresc = list()
                                                                                                                                                                                                                                                                                                           
  for i in lista_entrada:                                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                                                           
    #1) Lista Aleatória <- OBRIGATÓRIO(PEDIDO NA ATIVIDADE)                                                                                                                                                                                                                                                
    lista = list(range(0, i + 1))                                                                                                                                                                                                                                                                          
    random.shuffle(lista)
    tempos_orden_Random.append(timeit.timeit("heapSort({})".format(lista),setup="from __main__ import heapSort",number=1))
    num_iteracoes_Random.append(heapSort(lista))

    num_iteracoes = 0

    #2) Lista já ORDENADA em ordem DECRESCENTE<- OPCIONAL(AMOSTRAGEM DO ALUNO)                                                                                                                                                                                                                              
    lista = list(range(i,-1,-1))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    tempos_orden_Decresc.append(timeit.timeit("heapSort({})".format(lista),setup="from __main__ import heapSort",number=1))
    num_iteracoes_Decresc.append(heapSort(lista))

    num_iteracoes = 0
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   #                                                                                                                                                                                                                                                                                                            #
    #3) Lista já ORDENADA em ordem CRESCENTE<- OPCIONAL(AMOSTRAGEM DO ALUNO)                                                                                                                                                                                                                               
    lista = list(range(0,i+1,1))
    tempos_orden_Cresc.append(timeit.timeit("heapSort({})".format(lista),setup="from __main__ import heapSort",number=1))
    num_iteracoes_Cresc.append(heapSort(lista))

    num_iteracoes = 0
                                                                                                                                                                                                                                                                                                  
  desenhaGrafico2(lista_entrada,tempos_orden_Random,tempos_orden_Decresc,tempos_orden_Cresc,"GraficoHeapSort(Tamanho_Lista-X-Tempo_Ordenacoes).png", "Tempo(Lista->Aleatória[Heap Sort])","Tempo(Lista->Decrescente[Heap Sort])","Tempo(Lista->Crescente[Heap Sort])",'(Heap Sort - Listas: Aleatória/Decrescente/Crescente)Tamanho_Lista X Tempo_Ordenacoes','magenta','orange','black',"<Entradas/>","<Tempo-Saída/>")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           #                                                                                                                                                                                                                                                                                                           
  desenhaGrafico2(lista_entrada,num_iteracoes_Random,num_iteracoes_Decresc,num_iteracoes_Cresc,"GraficoHeapSort(Tamanho_Lista-X-Numero_Iteracoes).png", "SWAPS(Lista->Aleatória[Heap Sort])","SWAPS(Lista->Decrescente[Heap Sort])","SWAPS(Lista->Crescente[Heap Sort])",'(Heap Sort - Listas: Aleatória/Decrescente/Crescente)Tamanho_Lista X SWAPS','magenta','orange','black',"<Entradas/>","<Tempo-Saída/>")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           #                                                                                                                                                                                                                                                                                                           
#################################################################################################################################################################################################################################################################################################################################################################}

#Inicialização da aplicação:
##########################################################################
lista_teste = [100000,200000,400000,500000,1000000,2000000]              #
cria_Graficos(lista_teste)                                               #
##########################################################################
#############################
################                                                       
