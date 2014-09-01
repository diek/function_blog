
# Creating a function
A function in python is the most basic object we can call in Python. Python has a number of built in functions, the one we are most familiar with would have to be `print`. Python allows us to create our own custom functions. [Tutorial Point](http://www.tutorialspoint.com/python/python_functions.htm) defines a function nicely as "a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your application and a high degree of code reusing." 
From PyDocs, a note on what I mean by statement:
"Simple statements are comprised within a single logical line"

## Overall structure of a python function

![def name_function]
(https://raw.githubusercontent.com/diek/function_blog/master/_images/function_structure.png)

1. `def` is mandatory
2. function name, be descriptive, a good guide, 'what does the function do?'
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

1. "return leaves the current function call with the expression list (or None) as return value." For example:![main_sublime_text_3_screen](https://raw.githubusercontent.com/diek/function_blog/master/_images/demo_return.png) As demonstrated the print statement is never executed. The function evaluates the number, and once return is reached the expression is returned, 9 in the first example, and 7 in the second.

2. "When return passes control out of a try statement with a finally clause, that finally clause is executed before really leaving the function."

*Unless otherwise specified, this is based upon my notes, and lectures from Learn to Program: The Fundamentals by Jennifer Campbell, Paul Gries. Supplemented with info from PyDocs.*