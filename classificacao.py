porco1 = [1,1,0]
porco2 = [1,1,0]
porco3 = [1,1,0]
cachorro1 = [1,1,1]
cachorro2 = [0,1,1]
cachorro3 = [0,1,1]

dados = [porco1,porco2,porco3,
cachorro1,cachorro2,cachorro3]

marcacoes = [1,1,1,-1,-1,-1]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(dados,marcacoes)

misterioso1 = [1,1,1]
misterioso2 = [1,0,0]
misterioso3 = [0,0,1]

teste = [misterioso1,misterioso2,misterioso3]
marcacoes_teste = [-1,1,1]

resultado = modelo.predict(teste)
print(resultado)
diferenca = (resultado - marcacoes_teste)
acertos = [d for d in diferenca if d == 0]

taxa = 100.0 * len(acertos) / len(teste)
print(taxa)
