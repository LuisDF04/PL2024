import re

def convert_header(text):
    def repl(match):
        level = len(match.group(1))
        return f"<h{level}>{match.group(2)}</h{level}>"
    return re.sub(r'^(#{1,3})\s*(.+)', repl, text, flags=re.MULTILINE)

def convert_bold(text):
    return re.sub(r'\*\*(\w*)\*\*', r'<b>\1</b>', text, 0, 0)

def convert_italico(text):
    return re.sub(r'\*(\w*)\*', r'<i>\1</i>', text, 0, 0)

def convert_list(text):
    lines = text.split('\n')
    inside_list = False
    new_lines = []
    for line in lines:
        match = re.match(r'\s*(\d+)\.\s*(.+)', line)
        if match:
            if not inside_list:
                new_lines.append("<ol>")
                inside_list = True
            new_lines.append(f"<li>{match.group(2)}</li>")
        else:
            if inside_list:
                new_lines.append("</ol>")
                inside_list = False
            new_lines.append(line)
    if inside_list:
        new_lines.append("</ol>")
    return '\n'.join(new_lines)

def convert_link(text):
    return re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', text)

def convert_image(text):
    return re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', text)

def markdown_to_html(text):
    text = convert_header(text)
    text = convert_bold(text)
    text = convert_italico(text)
    text = convert_list(text)
    text = convert_link(text)
    text = convert_image(text)
    return text

md_text = """
# Título Principal
## Subtítulo
Texto com **negrito** e *itálico*.

1. Primeiro item
2. Segundo item
3. Terceiro item

Veja mais em [exemplo](http://example.com).
Ou esta imagem: ![Descrição](http://image.com)
"""

html_text = markdown_to_html(md_text)
print(html_text)