print('=-=-=-=-=-=-=-=-=-=-=-ELEIÇÕES 2024=-=-=-=-=-=-=-=-=-=-=-')

#interface principal do programa
while True:
        print('|1| fornecer a lista de candidatos \n|2| exibir as informações: nome, nome na urna, número e partido. \n|3| Gerar página HTML com estatísticas \n|4| sair')
        op = input('o que você deseja fazer? (digite abaixo o número da ação) \n--> ')
        match op:
            case '1':
                print('imprimindo lista de candidatos...')
                print('opção ainda não disponível')
            case '2':
                print('exibindo informações...')
                print('opção ainda não disponível')
            case '3':
                print('gerando página HTML...')
                print('opção ainda não disponível')
            case '4':
                print('fim do programa...')
                break
            case _:
                print('opção inválida')