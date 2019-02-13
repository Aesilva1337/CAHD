from keras.models import Sequential
from keras.layers import Dense
import numpy
import json, requests

numpy.random.seed(7)
#TODO
#Executa requisição para armazenamento de dados
# reponse = requests.get("urlAPI")
# dataset = json.loads(response.content)

#Carregada dados
dataset = numpy.loadtxt("DadosConsolidadosAPI.csv", delimiter=";", encoding='latin-1')

#Separa os dados, Sintomas de Resultados
#Sintomas
X = dataset[:,0:7]
#Diagnóstico/Classificção
Y = dataset[:,7:9]

#Arquitetura da rede neural
model = Sequential()
model.add(Dense(15, input_dim=7, activation='relu'))
model.add(Dense(15, activation='relu'))
model.add(Dense(15, activation='relu'))
model.add(Dense(15, activation='relu'))
model.add(Dense(15, activation='relu'))
model.add(Dense(9, activation='relu'))
model.add(Dense(2, activation='sigmoid'))
print(model)

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#Treinamento da inteligencia artificial
model.fit(X, Y, epochs=3, batch_size=10, verbose=2)

scores = model.evaluate(X, Y)
print("\n%s: %.2f%%\n" % (model.metrics_names[1], scores[1]*100))

#Pergunta os sintomas para execução do diagnostico e classificação a partir do dados obtidos
TS = [[]]
Questions = ['altura', 'peso', 'indice de massa', 'pressão sanguinea sistólica',
             'pressão sanguinea diastólica', 'triglicedis', 'colesterol']
for q in Questions:
    TS[0].append(input('Digite seu valor de ' + q + ': '))
    
predictions = model.predict(numpy.array(TS))

#TODO: Realizar requisição para Tradução
#Transaforma o resultado em algo paupavel para o usuario e printa na tela
print("\n*****************************************************************")
print("Resultado:-\n")
for result in predictions:
    classific = round(result[0])
    diag = round(result[1])
    
    print("Diagnóstico: ")
    print(diag)
    print(result[1])
    
    print(result[0])
    print("\nClassificação: ")
    print({
        0 : "Emergente",
        1 : "Muito Urgente",
        2 : "Urgente",
        3 : "Pouco Urgente",
        4 : "Não Urgente"
    }[classific])