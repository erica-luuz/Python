nome = 'Erica'  #String
nome_usuario = 'Erica Giselle'
print(nome)
print(nome_usuario)

media = 0  # Variavel do tipo numerico naousa aspas
n1 = n2 = n3 = n4 = 0.0
nome, idade = 'Benjamim', 8
estado = True

#Função type()   me mostra os tipos de variaveis atribuidos, estes sao tipos primitivos

print(type(media))
print(type(n3))
print(type(nome))
print(type(idade))
print(type(estado))
print(type(1+2j))

# Função Isinstance()  
a =10 
b = 'sol'
print(isinstance(a, int)) # Pegar a variavel "a" e vai comparar se é um inteiro, e dara o resultado True ou False
print(isinstance(b, float))
print(isinstance(a, (int,float))) # se é um dos dois, do mesmo grupo.

a = 40
c = 3
r = a * c
print(r)