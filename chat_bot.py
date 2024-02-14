import os

def processar_resposta(resposta, nome):
    if resposta == '1':
        print(f"{os.linesep}{nome}, O Brasil tem 5 títulos de Copa do Mundo!{os.linesep}")
    elif resposta == '2':
        print(f"{os.linesep}{nome}, O Brasil foi descoberto por Pedro Álvares Cabral em 1500.{os.linesep}")
    elif resposta == '3':
        print(f"{os.linesep}{nome}, A expectativa de vida no Brasil é de cerca de 75 anos.{os.linesep}")
    elif resposta == '4':
        print(f"{os.linesep}{nome}, A sigla RG significa Registro Geral.{os.linesep}")
    else:
        print("Digite um valor válido de 1 à 4!")

def start():

    print('Olá! Seja bem-vindo ao meu Chat Bot feito em Python')

    nome = input('Digite seu nome: ')

    email = input('Digite seu email: ')

    while True:

        resposta = input(
            f'O que tem interesse em saber hoje?{os.linesep}[1] - Quantas copas do mundo o Brasil tem?{os.linesep} 
            [2] - Quem descobriu o Brasil?{os.linesep}[3] - Qual a expectativa de vida no Brasil?{os.linesep} 
            [4] - O que significa a sigla RG?{os.linesep}')
        
        processar_resposta(resposta, nome)

if __name__ == '__main__':
    start()
