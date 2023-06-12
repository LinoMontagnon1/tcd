#TCD 2 e 3

# Import the regular expression module
import re

# Define the tokens using regular expressions
TOKENS = ('IDENTIFICADOR', 'NUMERO', 'OPERADOR', 'RELACIONAL', 'ATRIBUICAO', 'DELIMITADOR')
T_IDENTIFICADOR = r'[a-zA-Z]+'
T_NUMERO = r'[0-9]*[.]?[0-9]+'
T_OPERADOR = r'[*/+-]'
T_RELACIONAL = r'[><]=?|={2}|!='
T_ATRIBUICAO = r'={1}'
T_DELIMITADOR = r';'

# Define the comment types using regular expressions
COMENTARIOS = ('BLOCO', 'LINHA')
C_BLOCO = r'/\*.*?\*/'
C_LINHA = r'//.*'

# Define a function to get the input code from the user
def input_codigo():
    print('Coloque aqui o seu código. "Ctrl-Z + Enter" em uma linha vazia para salvar o código.')
    codigo = {}
    n = 1
    while True:
        try:
            linha = input()
            codigo[n] = linha
            n += 1
        except EOFError:
            break
    return codigo

# Define a function to output the input code
def output_codigo(codigo):
    print('\n--------------- SAIDA ---------------\n')
    for linha in codigo:
        print(f'{linha}: {codigo[linha]}')

# Define a function to generate a table of symbols
def tabela_simbolos(codigo):
    tabela = []
    for linha in codigo:
        conteudo = codigo[linha]
        while conteudo:
            match = None
            for token in TOKENS:
                padrao = globals().get(f'T_{token}')
                match = re.match(padrao, conteudo)
                if match:
                    valor = match.group(0)
                    conteudo = conteudo[len(valor):]
                    tabela.append([valor.strip(), token])   
                    break   
            if match is None:   
                conteudo = conteudo[1:]   
    return tabela


# Define a function to output the table of symbols
def output_tabela(tabela):
    print()
    print('========== TABELA DE SIMBOLOS ==========')
    for token, tok_type in tabela:
        print(f"{token} \t | \t {tok_type}")


# Define a function to remove spaces before and after each lexeme
def remover_espacos(codigo):
    for linha in codigo:
        codigo[linha] = re.sub(r'\s+', ' ', codigo[linha].strip())
    return codigo

# Define a function to remove comments from the input code
def remove_comentarios(codigo):
    for tipo in COMENTARIOS:
        padrao = globals().get(f'C_{tipo}')
        for linha in codigo:
            codigo[linha] = re.sub(padrao, '', codigo[linha], flags=re.DOTALL)
    codigo_str = '\n'.join(codigo.values())
    codigo_str = re.sub(r'/\*.*?\*/', '', codigo_str, flags=re.DOTALL)
    codigo = {i+1: linha for i, linha in enumerate(codigo_str.split('\n'))}
    return codigo

# Define the main function to compile the input code
def compilador(entrada):
    codigo = remove_comentarios(entrada)
    codigo = remover_espacos(codigo) 
    output_codigo(codigo)
    tab_simb = tabela_simbolos(codigo)
    output_tabela(tab_simb)

# Define the entry point of the program
if __name__ == '__main__':
    entrada = input_codigo()
    compilador(entrada)
