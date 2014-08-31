
# Creating a function
From PyDocs, a note on what I mean by statement:
"Simple statements are comprised within a single logical line"

## Overall structure of a python function

![def name_function]
(https://raw.githubusercontent.com/diek/function_blog/master/_images/function_structure.png)

1. `def` is mandatory
2. function name, be descriptive
3. parameters, inside of parenthesis, sometimes referred to as arguments:
	- parameters, may be none/zero, or 1, 2, 3, or more. If more than one, they must be separated by a comma.
  	- a parameter(s) is provided in the function call
4. docstring - optional but should be included, see [PEP 257 -- Docstring Conventions](http://legacy.python.org/dev/peps/pep-0257/) for more detail.
5. body:
	- heart of the function, like the engine, this is the mechanics and all the working parts.
	- made up of one or more statements
	- normally ends with a return statement, note that this is not always the case.
	- even if you do not use a return statement, python will return 'None'

### The return statement.


Two important points from PyDocs:

1. "return leaves the current function call with the expression list (or None) as return value."

2. "When return passes control out of a try statement with a finally clause, that finally clause is executed before really leaving the function."

*This is based upon my notes, and lectures from Learn to Program: The Fundamentals by Jennifer Campbell, Paul Gries. Supplemented with info from PyDocs.*