# Lexical Analyzer & Token Counter

## 1. Aim

To implement a lexical analyzer that reads source code from a user-specified input file, identifies different types of tokens, and counts the number of tokens in each category.

## 2. Description

This project is a simple **Compiler Design (CD) Lab** program implemented in Python.

The program asks the user to enter the name of the file containing the source code. It then reads the contents of that file and performs lexical analysis.

The program identifies the following token types:

* Keywords
* Identifiers
* Numbers
* Operators
* Delimiters

Finally, it displays each token along with its token type and prints the total count of each token category.

## 3. Requirements

* Python 3.x
* Command Prompt / Terminal
* No GCC or C compiler is required.

## 4. Project Structure

```text
CD_LAB/
│
├── lexer.py
├── input1.txt
└── input2.txt
```

* `lexer.py` - Main lexical analyzer program.
* `input1.txt` / `input2.txt` - Input files containing source code to be analyzed.

## 5. How to Run

### Step 1: Open Command Prompt

Open Command Prompt on Windows.

### Step 2: Navigate to the project folder

For example:

```text
cd Desktop\CD_LAB
```

### Step 3: Check Python

Run:

```text
python --version
```

If Python is installed, its version will be displayed.

### Step 4: Run the program

Execute:

```text
python lexer.py
```

The program will ask:

```text
Enter the input file name:
```

Enter the name of the input file, for example:

```text
input1.txt
```

## 6. Example Input

Suppose `input1.txt` contains:

```c
int a = 10;
int b = 20;
a = a + b;
```

## 7. Example Execution

Run:

```text
python lexer.py
```

Then enter:

```text
Enter the input file name: input1.txt
```

## 8. Example Output

```text
LEXICAL ANALYZER
-----------------------------
int             : KEYWORD
a               : IDENTIFIER
=               : OPERATOR
10              : NUMBER
;               : DELIMITER
int             : KEYWORD
b               : IDENTIFIER
=               : OPERATOR
20              : NUMBER
;               : DELIMITER
a               : IDENTIFIER
=               : OPERATOR
a               : IDENTIFIER
+               : OPERATOR
b               : IDENTIFIER
;               : DELIMITER

-----------------------------
TOKEN COUNTS
-----------------------------
Keywords    : 2
Identifiers : 5
Numbers     : 2
Operators   : 4
Delimiters  : 3
-----------------------------
```

## 9. Supported Tokens

### Keywords

The program recognizes keywords such as:

```text
int
float
char
double
if
else
for
while
do
return
void
main
```

### Identifiers

Identifiers are names used for variables, functions, etc.

Examples:

```text
a
total
number1
_student
```

### Numbers

The program recognizes integer and decimal numbers.

Examples:

```text
10
25
3.14
100
```

### Operators

The program recognizes operators such as:

```text
+
-
*
/
%
=
==
!=
<
>
<=
>=
```

### Delimiters

The program recognizes:

```text
;
,
(
)
{
}
[
]
```

## 10. Error Handling

If the entered file does not exist, the program displays:

```text
Error: File not found!
```

Make sure that the input file is in the same folder as `lexer.py`, or provide the correct file path.

## 11. Features

* Takes the input file name at runtime.
* Reads source code from a separate file.
* Identifies different types of tokens.
* Displays each token and its category.
* Counts keywords, identifiers, numbers, operators, and delimiters.
* Does not require GCC.
* Can analyze multiple input files without modifying the Python program.

## 12. Conclusion

The lexical analyzer successfully reads source code from a user-specified file, separates the source code into tokens, identifies their categories, and counts the number of tokens in each category. This demonstrates the basic working principle of the lexical analysis phase of a compiler.
