def move_operator(string):
    # Remover espaços em branco
    string = string.replace(" ", "")

    # Verificar se a string contém apenas operandos ou operadores
    if not all(char.isdigit() or char in "+-*/" for char in string):
        raise ValueError("A string deve conter apenas operandos ou operadores.")

    # Encontrar o último operador e mover uma casa à direita
    last_operator_index = max(string.rfind("+"), string.rfind("-"), string.rfind("*"), string.rfind("/"))
    if last_operator_index != -1:
        operador1 = string[last_operator_index]
        string = string[:last_operator_index] + string[last_operator_index + 1:]
        print(string + operador1)
    # Encontrar o primeiro operador e mover uma casa à direita        
    first_operator_index = max(string.rfind("+"), string.rfind("-"), string.rfind("*"), string.rfind("/"))
    if first_operator_index != -1:
        operador2 = string[first_operator_index]
        string = string[:first_operator_index] + string[first_operator_index+1:last_operator_index] + operador2 +string[last_operator_index:]
        print(string + operador1)

    first_operator_index = max(string.rfind("+"), string.rfind("-"), string.rfind("*"), string.rfind("/"))
    if first_operator_index != -1:
        operador2 = string[first_operator_index]
        string = string[:first_operator_index] +string[first_operator_index + 1:] + operador2
        print(string + operador1)
    return string

# Exemplo de uso
input_string = input("Digite a string de operandos e operadores: ")
try:
    resultado = move_operator(input_string)
except ValueError as e:
    print("Erro:", e)
