#basico
print("------------#numeros-----------------")
print(10 / 2)
print(10 // 2)
print(10 * 2)
print(10 ** 3)
print(10 % 3)

#string
print("------------#string-----------------")
x = "x:\numer"
print(x)
print("c:\numer")
print("c:\numer")
print(r"c:\numer")
print( (r"c:\numer") *2 )
name = "ilivanlton"
print(name[2])
print(name[0:2])
print('Seu saldo é %s' % 12)

#lista []
#recebe qualquer dado
print("------------#lista-----------------")
lista = [23,23,True,"sdfsd"]
lista.append(10)#adiciona ao final
print(lista)
print(lista[0])
lista.remove(10) #remove a primeira occorencia
del(lista[2])
print(lista)

#condicionais
print("------------#condicionais-----------------")

total = 101
if total > 100:
    print("maior")
elif total < 100:
    print("menor")
else:
    print("opss")

acc = '00-23'
pas = 2343
accounts = {
    '00-23':{
        'pass':2343
    },
    '00-24':{
        'pass':2343
    }
}

if acc in accounts and acc == accounts[acc]['pass']:
    print('Conta valida')
else:
    print('Conta invalida')

print('verdade' if True else 'falso')

#for
print("------------#for-----------------")
lista = [2, 4, 6, 8, 10]
for item in lista:
    print(item)

for item in lista[1:4]:
    print(item)

nomes = ["Wesley" , "Silva"]
for nome in nomes:
    if nome == "Wesley":
        print(nome)

for nome in nomes:
    if not nome == "Wesley":
        print(nome)

#While
print("------------#while-----------------")
numer = 3
while numer < 10:
    print(numer)
    numer += 1
    #break
else:
    print("o else")

#funcoes
print("------------#funcoes-----------------")
def call_numbers():
    for number in range(0,10):
        print(number)

call_numbers()

def calculator(x,y):
    print(x-y)

calculator(y=5,x=10)
calculator(10,5)

def calculator2(x=10,y=5):
    print(x-y)
# Resultado com valores padrões = 5
calculator2();
# Passando valor apenas para x | Resultado = 15
calculator2(20);
# Passando valor apenas para y | Resultado = 0
calculator2(y=10);


#dicionarios
"""
cars.keys() 	Retorna todas as chaves do dicionário
cars.values() 	Retorna todos os valores do dicionário
cars.["corola"] 	Retorna o valor referente a chave informada
"""
print("------------#dicionarios-----------------")
cars = {}
cars['corola'] = "red"
cars['fit'] = "green"
cars['320'] = "black"
print(cars)

# Declarando um dicionário usando dict
people = dict(Wesley='Father',Mariana="Mother",Sarah="baby")

# Declarando um dicionário com chaves
family = {
    'wesley' : 'Father'
}

# Verificando se existe uma chave antes de imprimir
if 'Wesley' in people:
    print(people['Wesley'])

#interando dicionarios
for key, value in cars.items():
    print(key + " - " + value)
