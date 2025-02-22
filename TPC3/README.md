# TPC3: Conversor de MarkDown para HTML
- Data de entrega: 2025-02-28
- Nome: Luis Enrique Díaz De Freitas
- Número de Aluno: A104000

![Minha Foto](https://avatars.githubusercontent.com/u/146751915?s=400&u=021c640f21daf0066dc714d7cf1d916fefbd29ea&v=4)

## Enunciado
Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" da Cheat Sheet: Cabeçalhos, Bold, Itálico, Lista numerada, Link e Imagem.

# Como funciona o programa?

### Objetivo:
O programa converte texto escrito em Markdown para HTML, processando diferentes elementos como cabeçalhos, negrito, itálico, listas numeradas, links e imagens.

### Fluxo do Programa:

1. **Processamento dos Elementos Markdown:**
    - O programa recebe um texto em Markdown e aplica funções específicas para converter cada elemento para HTML.
    - Expressões regulares (`re`) são utilizadas para identificar padrões e fazer as substituições necessárias.

2. **Funções Implementadas:**
    - `convert_header(text)`: Converte cabeçalhos Markdown (`#`, `##`, `###`) para tags HTML (`<h1>`, `<h2>`, `<h3>`).
    - `convert_bold(text)`: Converte texto entre `**...**` para `<b>...</b>`.
    - `convert_italico(text)`: Converte texto entre `*...*` para `<i>...</i>`.
    - `convert_list(text)`: Converte listas numeradas (`1. item`) para `<ol><li>...</li></ol>`.
    - `convert_link(text)`: Converte links no formato `[texto](URL)` para `<a href="URL">texto</a>`.
    - `convert_image(text)`: Converte imagens no formato `![alt](URL)` para `<img src="URL" alt="alt"/>`.

3. **Fluxo de Conversão:**
    - Cada função é aplicada sequencialmente ao texto.
    - No final, o texto convertido é retornado como HTML formatado.

### Exemplo de Uso:
Entrada em Markdown:
```markdown
# Título Principal
## Subtítulo
Texto com **negrito** e *itálico*.

1. Primeiro item
2. Segundo item
3. Terceiro item

Veja mais em [exemplo](http://example.com).
Ou esta imagem: ![Descrição](http://image.com)
```

Saída em HTML:
```html
<h1>Título Principal</h1>
<h2>Subtítulo</h2>
Texto com <b>negrito</b> e <i>itálico</i>.

<ol>
<li>Primeiro item</li>
<li>Segundo item</li>
<li>Terceiro item</li>
</ol>

Veja mais em <a href="http://example.com">exemplo</a>.
Ou esta imagem: <img src="http://image.com" alt="Descrição"/>
```

## Resultados Obtidos
- [TPC3.py](TPC3.py) - Código-fonte do programa.

