import json

def maqLigada(stock):
    print("maq: 2024-03-08, Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")

    saldo = 0
    while True:
        inputUtl = input(">> ")
        if inputUtl == "SAIR":
            print("maq: Pode retirar o troco: ", calcular_troco(saldo))
            print("maq: Até à próxima")
            break
        elif inputUtl == "LISTAR":
            print("cod    |  nome      |  quantidade  |  preço ")
            for produto in stock:
                print(f"{produto['cod'], produto['nome'], produto['quant'], produto['preco']}")
        elif inputUtl.startswith("MOEDA "):
            moedas = inputUtl[6:].split(",")
            for moeda in moedas:
                if moeda.endswith("e"):
                    moeda = int(moeda[:-1])
                elif moeda.endswith("c"):
                    moeda = int(moeda[:-1])/100
                saldo += moeda
            print(f"SALDO: {saldo}")
        elif inputUtl.startswith("SELECIONAR "):
            cod = inputUtl[11:]
            existe = False
            for produto in stock:
                if produto["cod"] == cod:
                    existe = True
                    if saldo > produto["preco"]:
                        saldo -= produto["preco"]
                        produto["quant"] -= 1
                        print(f"maq: Pode retirar o produto dispensado: {produto['nome']}") 
                        print(f"maq: Saldo = {saldo}")
                    elif produto['quant'] == 0:
                        print("maq: Produto esgotado")
                    else:
                        print("maq: Saldo insufuciente para satisfazer o seu pedido")
                        print(f"maq: Saldo = {saldo}; Pedido = {produto["preco"]}")
                    break
            if existe == False:
                print("maq: Produto inexiste")
    return stock

def calcular_troco(saldo):
    moedas = [1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]
    troco = []
    for moeda in moedas:
        quantidade = saldo // moeda
        if quantidade > 0:
            troco.append(f"{quantidade}x {moeda}c")
            saldo -= quantidade * moeda
    return ", ".join(troco)

def carregar_stock(ficheiro):
    """Carrega o stock a partir de um ficheiro JSON."""
    try:
        with open(ficheiro, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # Se o ficheiro não existir, retorna uma lista vazia

def guardar_stock(ficheiro, stock):
    """Guarda o stock num ficheiro JSON."""
    with open(ficheiro, 'w', encoding='utf-8') as f:
        json.dump(stock, f, indent=4, ensure_ascii=False)

# Nome do ficheiro JSON
FICHEIRO_STOCK = "stock.json"

# Carregar o stock ao iniciar o programa
stock = carregar_stock(FICHEIRO_STOCK)
stock = maqLigada(stock)

# Guardar o stock atualizado ao sair
guardar_stock(FICHEIRO_STOCK, stock)
