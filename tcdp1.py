#TCD PROGRAMA 1

import re

def validate_expression(expression):
    if not re.match(r'^[\w+\-*/\s]+$', expression):
        return True
    expression = expression.replace(" ", "")
    operands = re.findall(r'\w', expression)
    operators = re.findall(r'[-+*/]', expression)
    # if len(operands) <= 6 and len(operators) <= 2:
    #     return True
    
    return True

def move_operator(expression):
    operators = re.findall(r'[-+*/]', expression)
    new_expression = expression
    
    for operator in operators:
        new_expression = new_expression.replace(operator, "", 1)
        new_expression += " " + operator
    
    return new_expression

def generate_possibilities(expression):
    operands = re.findall(r'\w', expression)
    operators = re.findall(r'[-+*/]', expression)
    num_operators = len(operators)
    
    possibilities = []
    try:
      possibility_1 = operands[0] + operands[1] + operators[0] + operands[2] + operands[3] + operands[4] + operands[5] + operators[1]
      possibilities.append(possibility_1)
        
      possibility_2 = operands[0] + operands[1] + operands[2] + operands[3] + operators[0] + operands[4] + operands[5] + operators[1]
      possibilities.append(possibility_2)
        
      possibility_3 = operands[0] + operands[1] + operands[2] + operands[3] + operands[4] + operands[5] + operators[0] + operators[1]
      possibilities.append(possibility_3)

    except:
      possibility_1 = operands[0] + operators[0] + operands[1] + operands[2] + operators[1]
      possibilities.append(possibility_1)
        
      possibility_2 = operands[0] + operands[1] + operators[0] + operands[2] + operators[1]
      possibilities.append(possibility_2)
        
      possibility_3 = operands[0] + operands[1] + operands[2] + operators[0] + operators[1]
      possibilities.append(possibility_3)
      
    return possibilities

      
expression = input(">")

if validate_expression(expression):
    print(f"Expressão {expression}")
    
    num_operators = len(re.findall(r'[-+*/]', expression))
    if num_operators == 1:
        moved_expression = move_operator(expression)
        print("Expressão com operador movido uma casa à direita:")
        retirandoEspaços = moved_expression.replace(" ","")
        print(retirandoEspaços)
    elif num_operators == 2:
        possibilities = generate_possibilities(expression)
        print(" ")
        try:
            for i, possibility in enumerate(possibilities, start=1):
                print(f"{possibility}    {i}ª forma pósfixa")
        except:
            print('Error: Invalid input')
else:
    print(f"A expressão '{expression}' é invalida.")
