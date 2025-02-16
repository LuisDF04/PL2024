import re

def read_csv(file_path):
    pattern = re.compile(
        r'([^;]+);(?:".*?"|.*?);\d*;([^;]*);([^;]*);[^;]*;.*?(?:\n|$)',re.DOTALL         
    )

    # r'([^;]+);        - 1. Nome da obra (captura tudo até o primeiro `;`)
    # (?:".*?"|.*?);    - 2. Descrição (ignorada, mas aceita `"` e `\n`)
    # \d*;              - 3. Ano de criação (ignorado)
    # ([^;]*);          - 4. Período (capturado)
    # ([^;]*);          - 5. Compositor (capturado)
    # [^;]*;            - 6. Duração (ignorada)
    # .*?(?:\n|$)',     - 7. ID (ignorado, mas garante que a regex continue com o próximo registro)
    # re.DOTALL         - `re.DOTALL` permite capturar quebras de linha dentro da descrição

    compositores = set()
    periodos = dict()

    with open(file_path, "r", encoding="utf-8") as file:
        next(file)  # Ignoramos a primeira linha
        data = file.read()  # Lemos todo o ficheiro como so uma string

    for match in pattern.finditer(data):
        nome, periodo, compositor = match.groups()  # Obtemos os valores corretos
        compositores.add(compositor)
        if periodo in periodos:
            periodos[periodo].append(nome)
        else:
            periodos[periodo] = [nome]

    compositores = sorted(compositores)
    for periodo in periodos:
        periodos[periodo].sort()

    return compositores, periodos


def menu(compositores, periodos):
    option = 0
    while(option != 4):
            print("1 - Listar compositores")
            print("2 - Listar obras por período")
            print("3 - Obras catalogadas em cada período")
            print("4 - Sair")
            option = int(input("Escolha uma opção: "))

            match option:
                case 1:
                    print("Compositores:")
                    for compositor in compositores:
                        print(compositor)
                case 2:
                    for periodo, obras in periodos.items():
                        print(f"Obras en el período '{periodo}':\n{', '.join(obras)}")
                case 3:
                    for periodo, obras in periodos.items():
                        print(f"El período '{periodo}' tiene {len(obras)} obras.")

def main():
    
    file_path = "TPC2/obras.csv"

    compositores, periodos = read_csv(file_path)
    menu(compositores, periodos)

if __name__ == "__main__":
    main()



        





