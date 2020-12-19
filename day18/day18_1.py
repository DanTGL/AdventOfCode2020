import re

equations = open("day18/input").read().splitlines()

pattern = re.compile("[()*/+-]|[0-9]+")

op_precedence = {"+": 0, "-": 0, "*": 0, "/": 0, "(": 2, ")": 2}


def shunting_yard(eq, patt):
    operator_stack = []
    output = []
    for m in re.finditer(patt, eq):

        tok = m.group(0)
        if tok.isdecimal():
            output.append(int(tok))
        elif tok != "(" and tok != ")":
            while len(operator_stack) > 0 and (op_precedence[operator_stack[-1]] >= op_precedence[tok]) and operator_stack[-1] != "(":
                output.append(operator_stack.pop())
            operator_stack.append(tok)
        elif tok == "(":
            operator_stack.append(tok)
        else:
            while operator_stack[-1] != "(":
                output.append(operator_stack.pop())

            operator_stack.pop()

    while len(operator_stack) > 0:
        output.append(operator_stack.pop())

    return output

def interpret(rpn_result):
    output_stack = []
    for i in rpn_result:
        if isinstance(i, int):
            output_stack.append(i)
        else:
            num1 = output_stack.pop()
            num2 = output_stack.pop()

            if i == "+":
                output_stack.append(num1 + num2)
            elif i == "-":
                output_stack.append(num2 - num1)
            elif i == "*":
                output_stack.append(num1 * num2)
            else:
                output_stack.append(num2 / num1)

    return output_stack[0]


sum = 0
for i in equations:
    rpn_result = shunting_yard(i, pattern)
    sum += interpret(rpn_result)

print(sum)