import operator

def calculator():
    """A simple calculator that can perform basic arithmetic operations."""

    def get_precedence(op):
        if op in ['+', '-']:
            return 1
        if op in ['*', '/']:
            return 2
        if op == '^':
            return 3
        return 0

    def apply_op(operators, values):
        op = operators.pop()
        right = values.pop()
        left = values.pop()
        if op == '+':
            values.append(left + right)
        elif op == '-':
            values.append(left - right)
        elif op == '*':
            values.append(left * right)
        elif op == '/':
            values.append(left / right)
        elif op == '^':
            values.append(left ** right)

    def evaluate(expression):
        tokens = []
        i = 0
        while i < len(expression):
            if expression[i].isspace():
                i += 1
                continue
            if expression[i].isdigit() or (expression[i] == '.' and i + 1 < len(expression) and expression[i+1].isdigit()):
                j = i
                while j < len(expression) and (expression[j].isdigit() or expression[j] == '.'):
                    j += 1
                tokens.append(float(expression[i:j]))
                i = j
                continue
            if expression[i] in ['+', '-', '*', '/', '^', '(', ')']:
                tokens.append(expression[i])
                i += 1
                continue
            raise ValueError("Invalid character in expression")

        values = []
        ops = []

        for token in tokens:
            if isinstance(token, float):
                values.append(token)
            elif token == '(':
                ops.append(token)
            elif token == ')':
                while ops and ops[-1] != '(':
                    apply_op(ops, values)
                if not ops or ops[-1] != '(':
                    raise ValueError("Mismatched parentheses")
                ops.pop()
            else: # operator
                while (ops and ops[-1] != '(' and get_precedence(ops[-1]) >= get_precedence(token)):
                    apply_op(ops, values)
                ops.append(token)

        while ops:
            if ops[-1] == '(':
                raise ValueError("Mismatched parentheses")
            apply_op(ops, values)

        if len(values) != 1 or ops:
            raise ValueError("Invalid expression")

        return values[0]


    while True:
        print("Enter an expression (or 'quit' to exit):")
        expression = input()

        if expression.lower() == 'quit':
            break

        try:
            result = evaluate(expression)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    calculator()
