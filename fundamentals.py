### Variables
# Are containers that saves a value. It can be name however you want.
# Syntax:

# <variable_name> = <value>

# It could be a number, float number, string or a boolean.

int_variable = 3
float_variable = 3.14
string_variable = "Hello World!"
bool_variable = True # Or False

print(type(bool_variable))

## Constants.
# Are variables with their values that can only be assign one time in a program. Using the SCREAMING_SNAKE_CASE (upper case to the whole variable)
# in the variable will make a variable a constant.

IMPORTANT_YEAR = 2019

# Re-assignment will be allowed by the compiler & interpreter,
# but this is VERY strongly discouraged.
# Please don't do this, it could create problems in your program!

IMPORTANT_YEAR = 2010

## Functions
# A function is a series of instructions that are pre-coded to do an action.
# They are usually created when writing the keyword "def". Between of the parentheses,
# we can write the parameters that the function need in order to work.
# We can also define a default value to the parameter in case there is no value
# inside the parameter.

def say_hello(name = "person"):
    print(f"Hello {name}!")

# After creating the function, we can use/call it inside the code by writing the name
# of the function continued by parentheses () and if it needs it, the value of the arguments.

say_hello("Alex")

# It's important to know that, when writing a function and code in general,
# we need to respect the indentation so Python can read correctly each line.

# The "return" keyword explicitly returns a value as a result of a function.

def add_two_numbers(n1, n2):
    return n1 + n2
print(add_two_numbers(1, 2))

# We can also store a returned value of a function inside a variable.

function_value = add_two_numbers(7, 5)
print(f"The stored value is: {function_value} using the \"add_two_number()\" function.")

# We can also use the dot (.) to call a function inside a class or module.

sentence = "Working hard on learning programming."
print(str.upper(sentence))

# "sentence" is an instance of the "str" class, so we can call the .upper() function it directly from the variable.

print(sentence.upper())

## Comments
# This is a comment. The compiler doesn't read comments.

# Docstrings
# Is an optional commentary section that describes how the function works. It uses """ inside a function to document
# how a function works.

def complex(real = 0.0, imag = 0.0):
    """Form a complex number.

        Keyword Arguments:
            real (float): The real part of the number (default 0.0)
            imag (float): The imaginary part of the number (default 0.0)
            
    """
    complex_zero = 0.0
    if imag == 0.0 and real == 0.0:
        return complex_zero

# We can use the .__doc__ after the name of the function to access to the docstrings.

