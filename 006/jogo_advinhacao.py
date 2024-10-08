import random   
 
def adivinha():
    numero = random.randint(0,100)
    tentativa = 1
    valor = int(input('digite um palpite: '))
    while(valor != numero):
        tentativa += 1
        if valor < numero:
            print('O palpite', valor, 'é MENOR que o número.')
            valor = int(input('Digite outro palpite: '))
        else:
            print('O palpite', valor, 'é MAIOR que o número.')
            valor = int(input('Digite outro palpite: '))
    print('Parabéns, você acertou na tentativa:',tentativa)
 
adivinha()
