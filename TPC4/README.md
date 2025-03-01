# TPC4: Analisador Léxico

- **Data de entrega**: 2025-03-07
- **Nome**: Luis Enrique Díaz De Freitas
- **Número de Aluno**: A104000

![Minha Foto](https://avatars.githubusercontent.com/u/146751915?s=400&u=021c640f21daf0066dc714d7cf1d916fefbd29ea&v=4)

## Enunciado
Construir um analisador léxico para uma liguagem de query com a qual se podem escrever frases do
género:

```
# DBPedia: obras de Chuck Berry 
select ?nome ?desc where { 
    ?s a dbo:MusicalArtist. 
    ?s foaf:name "Chuck Berry"@en . 
    ?w dbo:artist ?s. 
    ?w foaf:name ?nome. 
    ?w dbo:abstract ?desc 
} LIMIT 1000 
```

## Como funciona o programa?

### Objetivo:
O analisador recebe um texto de consulta e identifica os tokens, categorizando cada elemento conforme sua classe sintática.

### Fluxo do Programa:

1. **Definição de Tokens:**
    - O analisador define tokens para elementos como `SELECT`, `WHERE`, `LIMIT`, variáveis, URIs, strings, números, e símbolos.
    - As expressões regulares (`re`) são utilizadas para identificar padrões.

2. **Funções Implementadas:**
    - `t_SELECT`, `t_WHERE`, `t_LIMIT`: Capturam palavras-chave da linguagem.
    - `t_VAR`: Identifica variáveis que começam com `?`.
    - `t_PREFIX`: Reconhece prefixos de URIs (`dbo:`, `foaf:`).
    - `t_URI`: Identifica URIs completas.
    - `t_STRING`: Captura strings entre aspas, opcionalmente seguidas de um idioma (`@en`).
    - `t_NUMBER`: Reconhece números inteiros.
    - `t_LBRACE`, `t_RBRACE`, `t_DOT`, `t_COLON`, `t_AT`: Capturam símbolos individuais.
    - `t_ignore`: Ignora espaços e quebras de linha.
    - `t_error`: Trata caracteres inválidos.
    - `t_COMMENT`: Ignora comentários iniciados com `#`.

3. **Execução:**
    - O analisador recebe um texto de consulta e percorre o código gerando uma lista de tokens reconhecidos.

### Exemplo de Uso:
Entrada:
```sparql
# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000
```

Saída esperada (lista de tokens):
```
LexToken(SELECT,'select',1,35)
LexToken(VAR,'?nome',1,42)
LexToken(VAR,'?desc',1,48)
LexToken(WHERE,'where',1,54)
LexToken(LBRACE,'{',1,60)
LexToken(VAR,'?s',1,67)
LexToken(A,'a',1,70)
LexToken(PREFIX,'dbo:',1,72)
...
LexToken(VAR,'?desc',1,197)
LexToken(RBRACE,'}',1,204)
LexToken(LIMIT,'LIMIT',1,206)
LexToken(NUMBER,1000,1,212)
```

## Resultados Obtidos
- [TPC4.py](TPC4.py) - Implementação do analisador léxico.

