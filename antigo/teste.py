

def cria_conta(numero,nome,saldo,limit):
    return {"numero":numero,"nome":nome,"saldo":saldo,"limit":limit}


def deposita(conta, valor):
    conta["saldo"] += valor


def saca(conta, valor):
    conta["saldo"] -= valor


def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))
