from dados import carregar_acessos
X,Y = carregar_acessos()

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(X,Y)

misterioso1 = [1,0,0]
misterioso2 = [0,1,0]
misterioso3 = [1,1,1]
teste = [misterioso1,misterioso2,misterioso3]

resultado = modelo.predict(teste)
print(resultado)