import csv 

def carregar_acessos():
    X = []
    Y = []

    arquivo = open('acesso.csv','rb')
    leitor = csv.reader(arquivo)
    #pular a primeira linha
    leitor.next()

    for home,funciona,contato,comprou in leitor:
        X.append([int(home),int(funciona),int(contato)])
        Y.append(int(comprou))

    return X, Y
