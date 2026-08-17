import re

# Ask the user for the input file name
filename = input("Enter the input file name: ")

try:
    # Open the file entered by the user
    with open(filename, "r") as file:
        data = file.read()

except FileNotFoundError:
    print("Error: File not found!")
    exit()

# Keywords
keywords = {
    "int", "float", "char", "double", "if", "else",
    "for", "while", "do", "return", "void", "main"
}

# Operators
operators = {
    "+", "-", "*", "/", "%", "=", "==", "!=",
    "<", ">", "<=", ">="
}

# Delimiters
delimiters = {
    ";", ",", "(", ")", "{", "}", "[", "]"
}

# Find tokens
tokens = re.findall(
    r'==|!=|<=|>=|[A-Za-z_][A-Za-z0-9_]*|\d+(?:\.\d+)?|[+\-*/%=<>;,(){}\[\]]',
    data
)

# Counters
keyword_count = 0
identifier_count = 0
number_count = 0
operator_count = 0
delimiter_count = 0

print("\nLEXICAL ANALYZER")
print("-----------------------------")

for token in tokens:

    if token in keywords:
        print(f"{token:<15} : KEYWORD")
        keyword_count += 1

    elif re.fullmatch(r'[A-Za-z_][A-Za-z0-9_]*', token):
        print(f"{token:<15} : IDENTIFIER")
        identifier_count += 1

    elif re.fullmatch(r'\d+(?:\.\d+)?', token):
        print(f"{token:<15} : NUMBER")
        number_count += 1

    elif token in operators:
        print(f"{token:<15} : OPERATOR")
        operator_count += 1

    elif token in delimiters:
        print(f"{token:<15} : DELIMITER")
        delimiter_count += 1

print("\n-----------------------------")
print("TOKEN COUNTS")
print("-----------------------------")
print("Keywords    :", keyword_count)
print("Identifiers :", identifier_count)
print("Numbers     :", number_count)
print("Operators   :", operator_count)
print("Delimiters  :", delimiter_count)
print("-----------------------------")