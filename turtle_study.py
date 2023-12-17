from turtle import Turtle

t = Turtle()

while True:
    frente_tras = input('Para qual direção devemos ir? "frente(f)" ou "para trás(t)":')
    if frente_tras == 'f':
        distancia_frente_tras = int(input('Quantos pixels devemos ir para a frente:'))
        rotacionar = input("Rotacionar para d: direita, e: esquerda ou n: não rotacionar?")
        if rotacionar == 'd':
            direita = int(input('Quantos pixels devemos rotacionar para a direita?:'))
            t.right(direita)
            t.forward(distancia_frente_tras)
        

            
        if rotacionar == 'e':
            esquerda = int(input('Qauntos pixels devemos rotacionar para a esquerda?'))
            t.left(esquerda)
            t.forward(distancia_frente_tras)
            
        
        if rotacionar == 'n':
            saida = input('Deseja continuar andando(s/ n):')
            t.forward(distancia_frente_tras)    
        
        
            
    elif frente_tras == 't':
         distancia_tras = int(input('Quantos pixels devemos ir para a trás:'))
         rotacionar = input("Rotacionar para d: direita, e: esquerda ou n: não rotacionar?")
         if rotacionar == 'd':
            direita_t = int(input('Quantos pixels devemos rotacionar para a direita?:'))
            t.right(direita_t)
            t.backward(distancia_tras)
         
                
         
    
            
         if rotacionar == 'e':
            esquerda_t = int(input('Quantos pixels devemos rotacionar para a esquerda?'))
            t.left(esquerda_t)
            t.backward(distancia_tras)
            
         
        
         if rotacionar == 'n':
            saida = input('Deseja continuar andando(s/ n):') 
            t.backward(distancia_tras)   
            
            
    saida = input('Deseja continuar andando(s/ n):')
    if saida == 's':
        continue
    elif saida == 'n':
        break
         
         
         
input()