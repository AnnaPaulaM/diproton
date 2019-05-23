# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 16:54:38 2019

@author: Kratos
"""


'Programa feito por Anna Paula Mendes.'

'------------------- Bibliotecas Importadas -------------------'

import math
import matplotlib.pyplot as plt


'------------------- Condições Iniciais -------------------'
R = 5.0            #Raio de um átomo de Ferro
d = 1.0            #Distância entre os prótons
Q = 26             #Número de prótons 
q = 1.43996444     #Carga de um próton
k = 1.0            #Constante Eletrostática
m = 931            #Massa de um Próton
M = 45 * m         #Massa do núcleo de Ferro com 24 prótons
npasso = 10000     #Número de passos
t = 1              #Tempo total
conttempo = 0.0    #Contador de tempo
dt = t/npasso      #Passo


#Parâmetros iniciais do próton e do núcleo.
#Estabelecemos 1 como o núcleo e 2 como o próton "positivo".
x1 = -R       #Posição inicial do núcleo no eixo x
y1 = 0.0       #Posição inicial do núcleo no eixo y

vo_n = 0.0     #Velocidade inicial do núcleo.

x2 = R         #Posição inicial do próton 2 no eixo x
y2 = d/2       #Posição inicial do próton 2 no eixo y

vox_p2 = 0.0   #Velocidade inicial do próton 2 no eixo x
voy_p2 = 0.0   #Velocidade inicial do próton 2 no eixo y

'-------------------------- Definição de Funções -----------------------------'

#Função que retorna o valor do módulo da diferença r - R.
def modulo_diferenca_posicao(par1_p, par2_p, par1_n, par2_n):
    
    #Criamos uma lista para armazenar os valores de D.
    lista_D = []
    
    #Definimos os vetores r e R em função dos parâmetros passados para a função.
    r = [par1_p, par2_p]
    R = [par1_n, par2_n]
    
    #Fazemos um loop para adicionar na lista D cada par r - R calculado.
    for r, R in zip(r, R):
        lista_D.append(R - r)
    
    #Elevamos cada item da lista D ao quadrado.
    lista_D_quadrado = [item*item for item in lista_D]
    
    #Calculamos o módulo de D.
    modulo_D = math.sqrt(sum(lista_D_quadrado))

    
    return modulo_D


#Função para calcular a aceleração do próton no eixo x.
def aceleracao_proton_x(x, modulo_diferenca):
    ax = ((k/m)*q*Q*x) / (modulo_diferenca**3)
    return ax


#Função para calcular a aceleração do próton no eixo y.
def aceleracao_proton_y(y, modulo_diferenca):
    ay = (((k/m)*q*Q*y) / (modulo_diferenca**3)) + (((k/m)*(q**2)) / (4*(y**2)))
    return ay


#Função para calcular a velocidade
def velocidade_proton(velocidade_inicial, aceleracao):
    velocidade = velocidade_inicial + (aceleracao * dt)
    return velocidade


#Função para calcular a posição do proton ou do nucleo.
def posicao_equacao(posicao_inicial, velocidade_inicial, aceleracao):
    pos = posicao_inicial + (velocidade_inicial*dt) + ((aceleracao*(dt**2))/2)
    return pos


#Função para calcular a velocidade ou aceleração do nucleo.
def par_nucleo(par):
    par_nucleo = 2*(m / M)*par
    return par_nucleo


#Função para transformar as listas em arquivos txt.            
def tabela(nome, lista): 
    arquivo = open(nome + '.txt', 'a')
    for i in range(len(lista)):
        arquivo.write(str(lista[i]) + '\n')
    arquivo.close


#Função para plotar o gráfico da trajetoria.   
def plot_grafico_trajetoria(x, y, xlabel, ylabel, title): 
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.savefig('Trajetoria.jpg')
    #plt.scatter(0,0, color='red')
    #plt.autoscale(enable=True, axis=u'both', tight=False)
    plt.show()
    
#Função para plotar gráficos com 2 linhas.   
def plot_grafico(x, y, xlabel, ylabel, num): 
    plt.plot(x, y)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.autoscale(enable=True, axis=u'both', tight=False)
    plt.savefig('pic'+str(num)+'.jpg')
    plt.show()
   
#Função para plotar gráficos com 3 linhas.
def plot_grafico2(par_1, par_2, par_3, xlabel, ylabel, legend1, legend2, title, num): 
    plt.plot(par_1, par_2, label = legend1)
    plt.plot(par_1, par_3, label = legend2)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.title(title)
    plt.autoscale(enable=True, axis=u'both', tight=False)
    plt.savefig('pic'+str(num)+'.jpg')
    plt.show()


'------------------- Listas Criadas -------------------'

#Listas para posição do próton 2.
posx_p2 = []
posy_p2 = []
posr_p2 = []

#Lista para posição do núcleo.
posx_n = []

#Listas para velocidade do próton 2.
velx_p2 = []
vely_p2 = []
velmodulo_p2 = []

#Lista para velocidade do núcleo.
velx_n = []

#Listas para aceleração do próton 2.
acelx_p2 = []
acely_p2 = []
acelmodulo_p2 = []

#Lista para aceleração do núcleo.
acelx_n = []

#Lista do tempo.
tempo = []

#Lista da energia.
energia = []


energia_inicial =  (2*k*q*Q)/modulo_diferenca_posicao(x2, y2, x1, y1) + (k*(q**2))/(2*y2)

'------------------- Laço de Repetição -------------------'

print('--------------------- Início do Processamento de Dados -------------------------')


while (t > conttempo):
    
    #Rodando as funções de aceleração.
    
    #Para o próton 2:
    modulo_diferenca = modulo_diferenca_posicao(x2, y2, x1, y1)
    ax_p2 = aceleracao_proton_x(x2, modulo_diferenca)
    ay_p2 = aceleracao_proton_y(y2, modulo_diferenca)
    amodulo_p2 = math.sqrt(ax_p2**2 + ay_p2**2)
    
    
    #Para o núcleo:
    ax_n = par_nucleo(ax_p2)
    
    #Rodando as funções para velocidade.
    
    #Para o próton 2:
    vx_p2 = velocidade_proton(vox_p2, ax_p2)
    vy_p2 = velocidade_proton(voy_p2, ay_p2)
    vmodulo_p2 = math.sqrt(vx_p2**2 + vy_p2**2)
    
    
    #Para o núcleo.
    vx_n = par_nucleo(vx_p2)
    
    #Rodando as funções de posição:
    
    #Para o próton 2:
    x_p2 = posicao_equacao(x2, vox_p2, ax_p2)
    y_p2 = posicao_equacao(y2, voy_p2, ay_p2)
    r_p2 = math.sqrt(x_p2**2 + y_p2**2)
    
 
    #Para o núcleo>
    x_n = posicao_equacao(x1, vo_n, ax_n)
    
    #Energia
    E = m*(vx_p2**2) + (M*(vx_n**2))/2 + (2*k*q*Q)/modulo_diferenca_posicao(x_p2, y_p2, x_n, y1) + (k*(q**2))/(2*y_p2)
    
    
    #Montando um vetor com os valores (x,y):
    vetor_p2_loop = [x_p2, y_p2]
    vetor_n_loop = [x_n, 0]
    energia_loop = E
    
    print('--------------------- t =', conttempo, '-------------------------' + '\n')
    print('Posição do Próton 2:', vetor_p2_loop)
    #print('Posição do Próton 3:', vetor_p3_loop)
    print('Posição do Núcleo:', vetor_n_loop)
    print('Energia no momento t:', E)
    print('----------------------------------------------------------')
    
    
#Preenchendo as listas:
    
    #Posição do próton 2:
    posx_p2.append(x_p2)
    posy_p2.append(y_p2)
    posr_p2.append(r_p2)
    
    #Posição do núcleo.
    posx_n.append(x_n)
    
    
    #Velocidade do próton 2:
    velx_p2.append(vx_p2)
    vely_p2.append(vy_p2)
    velmodulo_p2.append(vmodulo_p2)
    
    #Velocidade do núcleo:
    velx_n.append(vx_n)
    
    
    #Aceleração do próton 2:
    acelx_p2.append(ax_p2)
    acely_p2.append(ay_p2)
    acelmodulo_p2.append(amodulo_p2)
    
    #Aceleração do núcleo:
    acelx_n.append(ax_n)
    
    
    #Lista do tempo:
    tempo.append(conttempo)

    #Atualizando os valores
    
    #Velocidade do próton 2.
    vox_p2 = vx_p2
    voy_p2 = vy_p2
        
    #Velocidade do núcleo.
    vo_n = vx_n
    
    #Posição do próton 2.
    x2 = x_p2
    y2 = y_p2
      
    #Posição do núcleo.
    x1 = x_n
    
    #Energia
    energia.append(E)

    #Atualizando o tempo
    conttempo = conttempo + dt

print('--------------------- Fim do Processamento de Dados -------------------------')


'------------------- Criando arquivos txt com as Listas -------------------'

tabela('Lista x Próton 2', posx_p2)
tabela('Lista y Próton 2', posy_p2)
tabela('Lista r Próton 2', posr_p2)

tabela('Lista r Núcleo', posx_n)

tabela('Lista vx Próton 2', velx_p2)
tabela('Lista vy Próton 2', vely_p2)
tabela('Lista v Próton 2', velmodulo_p2)

tabela('Lista v Núcleo', velx_n)

tabela('Lista ax Próton 2', acelx_p2)
tabela('Lista ay Próton 2', acely_p2)
tabela('Lista a Próton 2', acelmodulo_p2)

tabela('Lista a Núcleo', acelx_n)

tabela('Lista tempo', tempo)


'------------------- Gráficos -------------------'
#Plotando os gráficos

plot_grafico_trajetoria(posy_p2, posx_p2, 'Posição x (fm)', 'Posição y (fm)', 'Trajetória do Próton 2')
plot_grafico2(tempo, velx_p2, vely_p2, 'v (c)', 't (fm/c)', 'vx', 'vy', 'Próton 2', 0)
plot_grafico2(tempo, acelx_p2, acely_p2, 'a (c^2/fm)', 't (fm/c)', 'ax', 'ay', 'Próton 2', 1) 
