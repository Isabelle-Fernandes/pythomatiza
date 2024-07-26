# Um novo paciente chamado João deu entrada no hospital.
# Ele tem 20 anos e é um novo paciente deste hospital.
# Defina variáveis para armazenar o nome deste paciente,
# sua idade e se ele é um novo paciente da instituição.
# Mostre no sistema todas estas informações coletadas.

# nome
# paciente
# name
nome_paciente = input('Qual é o seu nome: ') # str
idade = input('Qual é a sua idade: ') #int

while True:
    novo_paciente = input('Você já foi atendido neste hospital: (1 - Sim ou 0 - Não): ')
    if novo_paciente != '0' and novo_paciente != '1':
        print('Por favor responda apenas 0 ou 1.')
    else :
        if novo_paciente == "1":
            novo_paciente = 'é um novo paciente'
        else :
            novo_paciente = 'NÃO é um novo paciente'
        
        break

mensagem = 'o paciente ' + nome_paciente + ' de ' + str(idade) + ' anos ' + novo_paciente


print(mensagem)


