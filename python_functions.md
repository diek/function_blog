
# CREATING A FUNCTION - Part 1
For many of you python code was a series of code statements, with the highest level of organization being a code block. This script would be saved in a py file, becoming a python module.

Python provides some flexibility on the approach to solving a challenge. One route is the function. Functions can be combined and used to create powerful programs, even without the use of object oriented programming.

## Three Python Terms

### Statement
PyDocs, 'Simple statements are comprised within a single logical line', e.g. print 'python is fun'

### Module
The term module can be somewhat confusing, from PyDocs 'A module is a file containing Python definitions and statements.' Within a module you can have one or more statements, made up of variables, assignment statements, and a mixture of control constructs executed from top to bottom. The code, is a basic **script**. In your course, PR4E, I am sure you created many such modules. 

**Note**: Modules can also contain more advanced code, including functions and and classes

### Function
A function in python is the most basic object we can call in Python. Python has a number of built in functions, the one we are most familiar with would have to be `str(object='')` used in printing. Python allows us to create our own custom functions. [Tutorial Point](http://www.tutorialspoint.com/python/python_functions.htm) defines a function nicely as "a block of organized, reusable code that is used to perform a single, related action."

## Some Key Reasons to Use a Function
1. **Isolate and Reduce Complexity**, by breaking a problem into smaller manageable parts. But a key part of this is readable code, using descriptive function names and using DocString to document the code. Take assignment 9.4 for example. The problem was to prompt for a file, read the file, find lines starting with 'From ', create a dictionary to count e-mail addresses, then display the e-mail with the highest occurrence. Within a module I used 4 primary functions to solve this, in most cases shown on the group page we saw anywhere from 20 or more lines of code that simply started at the top and moved to the bottom, loops being the exception.   Using functions, we are not concerned with the inside, we just want to know does the function do what is required. If we look at the diagram, which is easier to understand? Four functions with descriptive names, or a wall of code. Again this is a simple assignment, imagine 500 or 10000 lines of code,  with no organization except for Python's code indentation. The function provides a logical method to organize code, and solve each part of the problem.
![def_name_function](https://raw.githubusercontent.com/diek/function_blog/master/_images/function_straightlinecode.png)

2. **Provide Abstraction to Code**, while this concept may sound complex, it is not, it essentially means that we separate the mechanics of what our code is doing from the actual use of the coded function. (A simple example of not abstracting code; in many of the assignments the values were hard coded into the code and stored in the python file. With abstraction this would not happen. Any values would be passed in, only when the function is called or invoked. More on that to come.)

3. **Avoid Duplicate Code**, separating the code logic from implementation allows reuse of a function as necessary. This is simple concept and a primary theme in coding style. And this goes directly to the Zen of Python, "Readability counts."

4. **Improve Debugging**, separating code into functions improves the ability to identify problems, errors and bottlenecks.

5. **Speed up Code**, putting code in a function is far more efficient memory wise.

**Note:** Steve McConnell wrote this great advice in <u>Code Complete</u>. "One of the strongest mental blocks to creating effective functions is a reluctance to create a simple function for a simple purpose. Constructing a whole function to contain two or three lines of code might seem like overkill, but experience shows how helpful a good small function can be. Small function offer several advantages. **One is that they improve readability**." That may not seem important now, but when you are writing larger programs it will certainly become clear.

## Overall structure of a python function

![def_name_function](https://raw.githubusercontent.com/diek/function_blog/master/_images/function_structure.png)

1. `def` is mandatory, as is the `:` ending the header
2. function name, be descriptive, a good guide, 'what does the function do?' Name is any legal Python name.
3. parameters, inside of parenthesis, sometimes referred to as arguments:
	- parameters, may be none/zero, or 1, 2, 3, or more. If more than one, they must be separated by a comma.
    - a parameter(s) is provided in the function call
4. DocString - optional but should be included, see [PEP 257 -- DocString Conventions](http://legacy.python.org/dev/peps/pep-0257/) for more detail. We are going to discuss in detail in Part 2. 
5. body:
	- heart of the function, like the engine, this is the mechanics and all the working parts.
	- made up of one or more statements
	- normally ends with a return statement, note that this is not always the case.
	- even if you do not use a return statement, python will return 'None'

### The return statement.


**Two important points from PyDocs:**

1. "Return leaves the current function call with the expression list (or None) as return value." As demonstrated below the print statement is never executed. The function evaluates the number, and once `return` is reached the expression is returned, 12 in the first example, and 18 in the second.

![main_sublime_text_3_screen](https://raw.githubusercontent.com/diek/function_blog/master/_images/demo_return.png) 

2. "When return passes control out of a try statement with a finally clause, that finally clause is executed before really leaving the function."

### Invoking(Calling) a function, the other half of abstraction
**Note**: Although a function can have zero parameters, the examples I am using will all have parameters. 
![def_get_age](https://raw.githubusercontent.com/diek/function_blog/master/_images/get_age.png)

In this example using the function get_age, we called the function in the Python shell by using `age = get_age(2014, 1985)`. Once we invoke the function, 2014 is bound to current_year and 1985 is bound to birth_year. In this simple case we only have one expression in the function body.

Within the body of the function expressions are evaluated until none remain. Again if the keyword **return** is reached, the execution of the function is terminated and the value returned. In cases where the key **return** is not used, Python returns `None` to the function call.

In this example, the keyword **return** was not used. The code calls `print` on the bound variable 'Derrick' and that is the only evaluated expression. In the Python Shell we can see that `None` is returned.
![def_no_return](https://raw.githubusercontent.com/diek/function_blog/master/_images/nil_return.png)

To summarize the function call, with the help Eric Grimson, the man who turned me into detective when necessary.

## Execution of Function Call	
1. 'Expressions	for each	parameter are evaluated, bound to formal parameter names of function'	
2. Control moves to first expression in function body

3. Each expression is executed until the `return` keyword reached (returning value of next expression) or no expressions	are left, resulting in the function returning `None`.

4. 'Invocation is bound to the returned value'. For example, if we had a function to add x and y, and we invoked sum = add_num(3, 4), then 7 would be bound.
 
5. 'Control transfers to next piece of code', if applicable.	

## Next Up - Function Recipe.

*Unless otherwise specified, this is based upon my notes, and lectures from Learn to Program: The Fundamentals by Jennifer Campbell, Paul Gries. and MITx: 6.00.1x Introduction to Computer Science and Programming Using Python with Eric Grimson, and supplemented with info from PyDocs.*