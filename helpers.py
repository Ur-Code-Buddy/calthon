def parse_nested_brakets(raw_expression):
    """
    parses a string expression containing and returns a nested list of that expression

    Args:
        expression (str): The string expression containing nested parentheses.

    Returns:
        list: a nested list representation of the expression.

    """
    expression = "".join(raw_expression.split() )
    stack = []  #for keeping track of nested expressions
    result = ''  #to add characters of present expression
    nested_expressions = []  #to store the nested expression 

    for char in expression:

        if char == '(':
            #start a new nested expression if theres a braket
            if result:
                nested_expressions.append(result)  #add characters in the nested expression
            result = ''  #reset the result string
            stack.append(nested_expressions)  #put it in the stack
            nested_expressions = []  #reset it for new expression

        elif char == ')':
            if result:
                nested_expressions.append(result)

            if stack:
                inner_expression = nested_expressions  #store the current nested expression
                nested_expressions = stack.pop()  #pop the previous nested expression 
                nested_expressions.append(inner_expression) 
            result = ''  #reset it for next expression

        else:
            #char is neighter an opening nor closing,store it in the result string
            result += char


    if result:
        nested_expressions.append(result)

    return nested_expressions

