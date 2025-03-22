from expr_anasin import parse
# expressions = ["2+3", "67-(2+3*4)", "(9-2)*(13-4)"]
# for expr in expressions:
#     parser = Parser(expr)
#     print(f"{expr} = {parser.parse()}")

linha = input("Introduza uma exp: ")
parse(linha)