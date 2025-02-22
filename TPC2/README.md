# TPC2: Análise de um dataset de obras musicais
- Data de entregue: 2025-02-21
- Nome: Luis Enrique Díaz De Freitas
- Número de Aluno: A104000




![Minha Foto](https://avatars.githubusercontent.com/u/146751915?s=400&u=021c640f21daf0066dc714d7cf1d916fefbd29ea&v=4)

## Enunciado
1. Neste TPC, é proibido usar o módulo CSV do Python;
2. Devera ser lido o dataset, processá-lo e criar os seguintes resultados:
- Lista ordenada alfabeticamente dos compositores musicais;
- Distribuição das obras por período: quantas obras catalogadas em cada período;
- Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras
desse período.

# Como funciona o programa?

### Objetivo:
Este programa foi desenvolvido para ler e processar um arquivo CSV contendo informações sobre obras musicais. Ele extrai dados sobre compositores, períodos de criação e nomes das obras, organiza essas informações e apresenta ao usuário por meio de um menu interativo.

### Fluxo do Programa:

1. **Leitura e Processamento do Arquivo CSV**:
    - O arquivo CSV contém dados sobre várias obras, incluindo o nome da obra, a descrição, o ano de criação, o período de criação, o compositor, a duração e o ID.
    - O arquivo é lido de uma vez, e a função `read_csv` usa uma expressão regular (`re`) para identificar e capturar as informações relevantes de cada obra. A regex foi configurada para ignorar a descrição, ano de criação, duração e o ID, já que não são necessários para o objetivo do programa.

2. **Extração de Dados**:
    - A função `read_csv` percorre o conteúdo do arquivo e aplica a expressão regular para capturar:
        - **Nome da obra**: O nome da peça musical.
        - **Período**: O período de criação da obra (por exemplo, "Barroco").
        - **Compositor**: O nome do compositor da obra.
    - As informações extraídas são armazenadas de maneira organizada:
        - **Compositores**: São armazenados em um conjunto (`set`), para evitar duplicatas, e posteriormente ordenados.
        - **Períodos**: São armazenados em um dicionário (`dict`), onde cada chave é um período e os valores são as obras relacionadas a esse período. Cada lista de obras é ordenada.

3. **Menu Interativo**:
    - Após ler o arquivo e processar as informações, o programa exibe um menu para o usuário escolher uma das opções:
        1. **Listar compositores**: Exibe uma lista de todos os compositores ordenados.
        2. **Listar obras por período**: Exibe as obras de cada período (organizadas por período).
        3. **Obras catalogadas em cada período**: Exibe a quantidade de obras por período.
        4. **Sair**: Encerra o programa.

4. **Estrutura do Menu**:
    - O menu é baseado em um loop que continua até que o usuário escolha a opção de sair (opção 4).
    - Para cada escolha, o programa imprime os resultados na tela, proporcionando uma forma simples de explorar os dados sobre as obras.

### Detalhes Técnicos:

- **Expressão Regular (`re`)**:
    - A expressão regular é usada para capturar as informações da linha no arquivo CSV. Ela foi projetada para lidar com casos em que a descrição pode conter quebras de linha (`\n`) ou aspas (`"`), mas esses detalhes não são importantes para a extração das informações principais (nome, período e compositor).
    - A regex usada é:
      ```python
      r'([^;]+);(?:".*?"|.*?);\d*;([^;]*);([^;]*);[^;]*;.*?(?:\n|$)'
      ```
      Cada parte da expressão regular tem um papel específico:
        - **([^;]+)**: Captura o nome da obra (até o primeiro ponto e vírgula).
        - **(?:".*?"|.*?)**: Ignora a descrição (permitindo que ela contenha aspas ou não).
        - **\d***: Ignora o ano de criação.
        - **([^;]*)**: Captura o período.
        - **([^;]*)**: Captura o compositor.
        - **[^;]*;**: Ignora a duração.
        - **.*?(?:\n|$)**: Ignora o ID e permite que a regex capture até o final da linha ou até o próximo registro.

- **Estrutura de Dados**:
    - **Conjunto (`set`)**: Para garantir que não haja compositores repetidos, usamos um `set`, que automaticamente elimina duplicatas. Após isso, os compositores são ordenados para exibição.
    - **Dicionário (`dict`)**: Os períodos são armazenados em um dicionário, com as chaves sendo os períodos de criação e os valores sendo listas das obras desse período. Cada lista de obras é também ordenada para facilitar a visualização.

## Resultados obtidos

- [TPC2.py](TPC2.py) – Código-fonte do programa.
- [obras.csv](obras.csv) – Arquivo de entrada contendo os dados para processamento.
