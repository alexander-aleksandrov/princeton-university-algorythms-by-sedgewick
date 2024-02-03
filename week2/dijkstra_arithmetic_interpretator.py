def evaluate(expression):
    
    def operate(number1, number2, operator):
        if operator == "+":
            return number1 + number2
        elif operator == "-":
            return number1 - number2
        elif operator == "*":
            return number1 * number2
        elif operator == "/":
            return number1 / number2

    numbers = []
    operators = []
    for i in expression.replace(" ", ""):
        if i == "(": pass
        elif i in "+-*/": 
            operators.append(i)
        elif i.isdigit():
            numbers.append(int(i))
        elif i == ")":
            operator = operators.pop()
            number1 = numbers.pop()
            number2 = numbers.pop()
            numbers.append(operate(number2, number1, operator))        
    return numbers.pop()    