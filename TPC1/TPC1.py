def somador_on_off(texto):
    palavras = texto.split(" ")

    somaTotal = 0
    comportamento = True

    for palavra in palavras:

        # print(palavra)

        if palavra.lower() == "on":
            comportamento = True
            
        elif palavra.lower() == "off":
            comportamento = False
        
        elif palavra == "=":
            print(somaTotal)
        
        elif palavra.isdigit() and comportamento:
            somaTotal += int(palavra)
            
texto = "10 abc 20 On 5 off 30 = 15 On 10 = Off 50 ="
print(texto)
somador_on_off(texto)