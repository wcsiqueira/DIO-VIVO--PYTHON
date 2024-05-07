produto = 10 
produto2 = 20

# operadores de comparação  
# igual
 print(produto == produto2) # False 
 #maior
 print(produto<produto2) # True

 print(produto>produto2)    # False
 #Menor ou igual
 print(produto<=produto2)   # True
 #Maior ou igual
print(produto>=produto2)   # False
 
print(produto!=produto2)   # True  
 
 # atribuição simples (=) ex: saldo = 500
 #modulo
 saldo %= 200
 #Divisão inteira
 saldo2 //=5
 #exponenciação
 saldo **= 2
 #operadores deLogicos 
 #or , not ,and 
 
 #Operadores de identidade 
 #is, is not 
 #Operadores de asssociação 
 #saber se a palavra está presente na strint  utilizando operadores de associação 
 
 def insere(estrutura, elemento):
    estrutura.append(elemento)
    return estrutura

def remove(estrutura):
    if len(estrutura) > 0:  # Verifica se a estrutura não está vazia
        return estrutura.pop(0)
    else:
        print("ERROR: A estrutura está vazia")
        return None  # Retorna None se a estrutura estiver vazia

estrutura = []
insere(estrutura, 1)
insere(estrutura, 22)
insere(estrutura, 333)
insere(estrutura, 4444)
while len(estrutura) > 0:
    print(remove(estrutura))

       