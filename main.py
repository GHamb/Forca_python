from random import *

banco = ['barco', 'casa', 'tijolo', 'agua', 'golfinho', 'carro', 'batente', 'jaguar',
         'lagarto', 'baleia', 'papagaio', 'elefante', 'porta', 'tartaruga', 'rosquinha', 'panetone']

escolha = randrange(0, len(banco))
resposta = banco[escolha]
vidas = 5
#print(resposta)
nlt = len(banco[escolha])
acerto = []
erros = 5

game = input('Deseja Jogar Forca ? (sim ou nao):')

if game == 'sim' or game == 'SIM' or game == 's':
    print('Palavra selecionada vamos iniciar!')
    print('A palavra tem {} letras'.format(nlt))
    while True:
        temp = []
        resultado = resposta
        for letra in resposta:
            if letra not in acerto:
                resultado = resultado.replace(letra, '_')
        print(resultado)
        letrav = input('digite uma letra:')
        for letras in resposta:
            if letras == letrav:
                # print(letrav)
                if letrav not in acerto:
                    temp.append(letrav)
                else:
                    print('Letra ja digitada')
        if temp:
            for letra in temp:
                acerto.append(letra)
                # print(acerto)
        if letrav in acerto:
            pass
        else:
            erros -= 1
            print('tentativa errada faltam {} tentativas'.format(erros))
            if erros == 0:
                print('você perdeu')
                break
        if len(acerto) == len(resposta):
            print('você acertou a palavra é {}'.format(resposta.upper()))
            break
if game == 'nao' or game == 'NAO' or game == 'n':
    quit()
