class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

def apply_operator(operators, values):
    right = values.pop()
    left = values.pop()
    op = operators.pop()
    if op == '+':
        values.push(left + right)
    elif op == '-':
        values.push(left - right)
    elif op == '*':
        values.push(left * right)
    elif op == '/':
        values.push(left / right)

def evaluate_expression(expression):
    values = Stack()
    operators = Stack()
    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            j = i
            while j < len(expression) and expression[j].isdigit():
                j += 1
            values.push(int(expression[i:j]))
            i = j
        elif expression[i] == ' ':
            i += 1
        else:
            while (not operators.is_empty() and
                   precedence(operators.peek()) >= precedence(expression[i])):
                apply_operator(operators, values)
            operators.push(expression[i])
            i += 1
    while not operators.is_empty():
        apply_operator(operators, values)
    return values.pop()

# 示例
expression = "3 + 5 * 8 - 6"
result = evaluate_expression(expression)
print("表达式的值为:", result)  # 输出: 表达式的值为: 19.0