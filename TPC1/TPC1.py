# def somador_on_off(texto):
#     palavras = texto.split(" ")

#     somaTotal = 0
#     comportamento = True

#     for palavra in palavras:

#         # print(palavra)

#         if palavra.lower() == "on":
#             comportamento = True
            
#         elif palavra.lower() == "off":
#             comportamento = False
        
#         elif palavra == "=":
#             print(somaTotal)
        
#         elif palavra.isdigit() and comportamento:
#             somaTotal += int(palavra)
            
# texto = "10 abc 20 On 5 off 30 = 15 On 10 = Off 50 ="
# print(texto)
# somador_on_off(texto)

def somador_on_off(texto):
    somaTotal = 0
    comportamento = True
    possível_comando = False
    numero_atual = ""

    for caractere in texto:
        if caractere.isdigit():
            #print(caractere)
            numero_atual += caractere  # Construímos o número caractere por caractere
        else:
            if numero_atual:  # Se havia um número acumulado, somamos se permitido
                if comportamento:
                    #print(numero_atual)
                    somaTotal += int(numero_atual)
                numero_atual = ""  # Resetamos para ler o próximo número

            if caractere.lower() == "o":  # Pode ser início de "on" ou "off"
                if texto[texto.index(caractere):texto.index(caractere) + 2].lower() == "on":
                    comportamento = True
                possível_comando = True
            elif caractere.lower() == "f":  # Pode ser início de "off"
                if possível_comando and texto[texto.index(caractere):texto.index(caractere) + 2].lower() == "ff":
                    comportamento = False
                    #print("false")
            elif caractere == "=":
                print(somaTotal)

# Exemplo de entrada sem espaços
texto = "35offonOff=holkfkfa24off20=11"
# texto = "10 abc 20 On 5 off 30 = 15 On 10 = Off 50 ="

print("Texto de entrada:", texto)
somador_on_off(texto)
