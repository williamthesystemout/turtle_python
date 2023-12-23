from turtle import Turtle

t= Turtle()
t.speed(1)

def quantidade_para_frente():
    respondendo = int(input('Quantos pixels devemos ir para frente? '))
    return respondendo

def quantidade_para_tras():
    respondendo = int(input('Quantos pixels devemos movimentar para trás? '))
    return respondendo

def rotacionar(turtle):
    rotacionando = input('Rotacionar a direita(d), esquerda(e) ou não rotacionar(n)? ')
    if rotacionando == 'd':
        rotacionar_para_direita(turtle)
    if rotacionando == 'e':
        rotacionar_para_esquerda(turtle)
           
def rotacionar_para_direita(turtle):
    rotacao_direita = int(input('Quantos pixels devemos ir para a direita? '))
    t.right(rotacao_direita)

def rotacionar_para_esquerda(turtle):
    rotacao_esquerda = int(input('Quantos pixels devemos ir para a esquerda? '))
    t.left(rotacao_esquerda)
     

while True:
    frente_ou_tras = input('Para qual direção ir? (F) ou (T)? ')

    if frente_ou_tras == 'F' or frente_ou_tras == 'f':
        pixels_para_frente = quantidade_para_frente()
        rotacionar(t)
        t.forward(pixels_para_frente)


    if frente_ou_tras == 't' or frente_ou_tras == 'T':
        pixels_para_tras = quantidade_para_tras()
        rotacionar(t)
        t.backward(pixels_para_tras)
    
    resposta = input('Deseja continuar andando(S / N)? ')
    
    if resposta not in ('sim','s'):
        break

    
