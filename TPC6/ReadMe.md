# Parser LL(1) Recursivo Descendente

- **Data de entrega**: 2025-03-21
- **Nome**: Luis Enrique Díaz De Freitas
- **Número de Aluno**: A104000


![Minha Foto](https://avatars.githubusercontent.com/u/146751915?s=400&u=021c640f21daf0066dc714d7cf1d916fefbd29ea&v=4)

## Enunciado
Baseado nos materiais fornecidos na aula, cria um parser LL(1) recursivo descendente que reconheça expressões aritméticas e calcule o respetivo valor.

Exemplos de expressões suportadas:
```
2+3
67-(2+3*4)
(9-2)*(13-4)
```

## Como funciona o programa?

### Objetivo:
O programa recebe uma expressão matemática como entrada e a processa usando um analisador sintático recursivo descendente, retornando o resultado final da avaliação.

## Gramática utilizada

```
E  → T E'      (expressão → termo seguido de soma ou subtração)
E' → '+' T E'  (continuação da expressão)
    | '-' T E'
    | ε        (expressão pode terminar)
T  → F T'      (termo → fator seguido de multiplicação ou divisão)
T' → '*' F T'  (continuação do termo)
    | '/' F T'
    | ε        (termo pode terminar)
F  → NUM       (fator pode ser um número)
    | '(' E ')' (ou uma subexpressão entre parênteses)
```

### Fluxo do Programa:
1. **Análise Léxica:**
    - A entrada é processada pelo `lexer`, que identifica os tokens (`NUM`, `PLUS`, `MINUS`, `TIMES`, `DIV`, `LPAREN`, `RPAREN`).
2. **Análise Sintática:**
    - O parser recursivo descendente segue as regras da gramática LL(1) para construir e avaliar a expressão.
3. **Execução:**
    - A árvore sintática abstrata (AST) é processada e o resultado da expressão é calculado.

### Funções Implementadas:
- **`parse(data)`** → Inicia a análise sintática da expressão.
- **`expr()`** → Processa `E → T E'`, lidando com soma e subtração.
- **`term()`** → Processa `T → F T'`, lidando com multiplicação e divisão.
- **`factor()`** → Processa `F → NUM | '(' E ')'`.
- **`rec_term(simb)`** → Verifica e consome tokens da entrada.

### Exemplo de Uso:
Entrada:
```
(9-2)*(13-4)
```
Saída esperada:
```
Analisando expressão: (9-2)*(13-4)
Derivando por P1: expr --> term expr'
Derivando por P4: term --> factor term'
Derivando por P8: factor --> '(' expr ')'
...
...
...
Expressão '(9-2)*(13-4)' avaliada como: 63
```

## Resultados Obtidos
- **[expr_analex.py](expr_analex.py)** - Implementação do analisador léxico.
- **[expr_anasin.py](expr_anasin.py)** - Implementação do parser recursivo descendente.
- **[expr_program.py](expr_program.py)** - Programa principal que executa o parser.

