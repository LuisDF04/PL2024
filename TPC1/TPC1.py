def somador_on_off(ficheiro):
    try:
        with open(ficheiro, 'r', encoding='utf-8') as text:
            somaTotal = 0
            comportamento = True
            
            for linea in text:
                numero_atual = ""
                posivel_comando = ""
                
                for i, caractere in enumerate(linea):
                    if caractere.isdigit():
                        numero_atual += caractere  # Construimos el número carácter por carácter
                    else:
                        if numero_atual:  # Si había un número acumulado, lo sumamos si está permitido
                            if comportamento:
                                somaTotal += int(numero_atual)
                            numero_atual = ""  # Reiniciamos para leer el siguiente número

                        if linea[i:i+2].lower() == "on":
                            comportamento = True
                            posivel_comando = ""
                        elif linea[i:i+3].lower() == "off":
                            comportamento = False
                            posivel_comando = ""
                        
                        if caractere == "=":
                            print(somaTotal)
    except FileNotFoundError:
        print(f"Erro: Não foi encontrado o ficheiro: '{ficheiro}'")
    except Exception as e:
        print(f"Erro: {e}")

# Uso de la función
document = "text.txt"  # Cambia esto con el nombre de tu text
somador_on_off(document)
