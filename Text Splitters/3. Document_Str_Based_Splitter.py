##  Used for splitting codes and markdowns and underneath we are using Reccursive splitters only but only thing here is we are specifying other seperators.

from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

text = """
class Calculator:
    def __init__(self):
        print("Calculator initialized!")

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error! Division by zero."

calc = Calculator()
print("Addition:", calc.add(10, 5))
print("Subtraction:", calc.subtract(10, 5))
print("Multiplication:", calc.multiply(10, 5))
print("Division:", calc.divide(10, 5))

"""
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size = 100,
    chunk_overlap = 0,
)

result = splitter.split_text(text)

print(result[1])