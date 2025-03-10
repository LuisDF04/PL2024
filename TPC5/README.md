# Simulador de Máquina de Vending

- **Data de entrega**: 2025-03-14
- **Nome**: Luis Enrique Díaz De Freitas
- **Número de Aluno**: A104000

![Minha Foto](https://avatars.githubusercontent.com/u/146751915?s=400&u=021c640f21daf0066dc714d7cf1d916fefbd29ea&v=4)

## Enunciado
A máquina tem um stock de produtos: uma lista de triplos, nome do produto, quantidade e preço.
 stock = [ 
    {"cod": "A23", "nome": "água 0.5L", "quant": 8, "preco": 0.7}, 
    ... 
] 
Podes persistir essa lista num ficheiro em JSON que é carregado no arranque do programa e é atulizado
quando o programa termina.
A seguir apresenta-se um exemplo de uma interação com a máquina, assim que esta é ligada, para que
possas perceber o tipo de comandos que a máquina aceita (as linhas iniciadas marcadas com 
">>" representam o input do utilizador):
``` 
maq: 2024-03-08, Stock carregado, Estado atualizado. 
maq: Bom dia. Estou disponível para atender o seu pedido. 
>> LISTAR 
maq: 
cod    |  nome      |  quantidade  |  preço --------------------------------- 
A23       água 0.5L    8              0.7 
... 
>> MOEDA 1e, 20c, 5c, 5c . 
maq: Saldo = 1e30c 
>> SELECIONAR A23 
maq: Pode retirar o produto dispensado "água 0.5L" 
maq: Saldo = 60c 
>> SELECIONAR A23 
maq: Saldo insufuciente para satisfazer o seu pedido 
maq: Saldo = 60c; Pedido = 70c 
>> ... 
... 
maq: Saldo = 74c 
>> SAIR 
maq: Pode retirar o troco: 1x 50c, 1x 20c e 2x 2c. 
maq: Até à próxima 
```

O stock encontra-se inicialmente armazenado num ficheiro JSON de nome "stock.json " que é carregado
em memória quando o programa arranca. Quando o programa termina, o stock é gravado no mesmo
ficheiro, mantendo assim o estado da aplicação entre interações.
Use a imaginação e criatividade e tente contemplar todos os cenários, por exemplo, produto inexistente ou
stock vazio.
Como extra pode adicionar um comando para adicionar alguns produtos ao stock existente (produtos
novos ou já existentes).
## Como funciona o programa?

### Objetivo:
O programa permite a simulação de uma máquina de vending, gerindo um stock de produtos e permitindo operações como inserção de moedas, compra de produtos e cálculo de troco.

### Fluxo do Programa:

1. **Carregamento do Stock:**
    - O programa inicia carregando os produtos do ficheiro `stock.json`.
    - Caso o ficheiro não exista, um stock vazio é assumido.

2. **Interação com o Utilizador:**
    - O programa exibe uma mensagem de boas-vindas e aguarda comandos do utilizador.
    - Os comandos disponíveis são:
      - `LISTAR`: Exibe a lista de produtos disponíveis.
      - `MOEDA <valores>`: Permite inserir moedas na máquina.
      - `SELECIONAR <código>`: Seleciona um produto para compra.
      - `SAIR`: Encerra o programa e devolve o troco.

3. **Funções Implementadas:**
    - `carregar_stock(ficheiro)`: Lê o stock do ficheiro JSON.
    - `guardar_stock(ficheiro, stock)`: Guarda o stock atualizado no ficheiro JSON.
    - `maqLigada(stock)`: Gerencia a interação do utilizador com a máquina.
    - `calcular_troco(saldo)`: Calcula o troco a devolver ao utilizador.

### Exemplo de Uso:

Entrada do utilizador:
```
maq: Bom dia. Estou disponível para atender o seu pedido.
>> LISTAR
maq:
cod    |  nome      |  quantidade  |  preço
A23       água 0.5L    8              0.7
>> MOEDA 1e, 20c, 5c, 5c
maq: Saldo = 1e30c
>> SELECIONAR A23
maq: Pode retirar o produto dispensado "água 0.5L"
maq: Saldo = 60c
>> SAIR
maq: Pode retirar o troco: 1x 50c, 1x 10c.
maq: Até à próxima
```

## Resultados Obtidos
- [TPC5.py](TPC5.py) - Implementação do analisador léxico.
- [stock.json](stock.json) - Stock de produtos: uma lista de triplos, nome do produto, quantidade e preço.

