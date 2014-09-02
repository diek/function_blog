
# Creating a function
For many of you python code was a series of code statements, with the highest level of organization being a code block. This script would be saved in a py file, becoming a python module.

Python has a great deal of flexibility on how we approach solving a challenge. 

## Some Python Terms

### Statement
"Simple statements are comprised within a single logical line"

### Module
The term module can be somewhat confusing, from PyDocs 'A module is a file containing Python definitions and statements.' Within a module you can have one or more statements, made up of variables, assignment statements, and a mixture of control constructs executed from top to bottom. The code, a basic **script**. In your course, PRE4, I am sure you created many such modules. One caution on naming your module, do not use the name of an existing python module, math.py for example. Modules can also contain more advanced code, including functions and and classes

### Function
A function in python is the most basic object we can call in Python. Python has a number of built in functions, the one we are most familiar with would have to be `print`. Python allows us to create our own custom functions. [Tutorial Point](http://www.tutorialspoint.com/python/python_functions.htm) defines a function nicely as "a block of organized, reusable code that is used to perform a single, related action."

## Some key reasons to use a Function
1. **Isolate and reduce complexity**, by breaking a problem into smaller manageable parts.
2. **Speed up Code**, putting your code in a function is far more efficient memory wise.
3. **Avoid duplicate code**, a simple concept and a primary theme in coding style. And this goes directly to the Zen of Python, "Readability counts."

**Note:** Steve McConnell wrote this great advice in <u>Code Complete</u>."One of the strongest mental blocks to creating effective functions is a reluctance to create a simple function for a simple purpose. Constructing a whole function to contain two or three lines of code might seem like overkill, but experience shows how helpful a good small function can be. Small function offer several advantages. **One is that they improve readability**." That may not seem important now, but when you are writing larger programs it will certainly become clear.

## Overall structure of a python function

![def_name_function](https://raw.githubusercontent.com/diek/function_blog/master/_images/function_structure.png)

1. `def` is mandatory, as is the `:` ending the header
2. function name, be descriptive, a good guide, 'what does the function do?' Name is any legal Python name.
3. parameters, inside of parenthesis, sometimes referred to as arguments:
	- parameters, may be none/zero, or 1, 2, 3, or more. If more than one, they must be separated by a comma.
    - a parameter(s) is provided in the function call
4. docstring - optional but should be included, see [PEP 257 -- Docstring Conventions](http://legacy.python.org/dev/peps/pep-0257/) for more detail. We are going to discuss this later. 
5. body:
	- heart of the function, like the engine, this is the mechanics and all the working parts.
	- made up of one or more statements
	- normally ends with a return statement, note that this is not always the case.
	- even if you do not use a return statement, python will return 'None'

### The return statement.


Two important points from PyDocs:

1. "return leaves the current function call with the expression list (or None) as return value." As demonstrated below the print statement is never executed. The function evaluates the number, and once `return` is reached the expression is returned, 12 in the first example, and 18 in the second.

![main_sublime_text_3_screen](https://raw.githubusercontent.com/diek/function_blog/master/_images/demo_return.png) 

2. "When return passes control out of a try statement with a finally clause, that finally clause is executed before really leaving the function."

*Unless otherwise specified, this is based upon my notes, and lectures from Learn to Program: The Fundamentals by Jennifer Campbell, Paul Gries. Supplemented with info from PyDocs.*