# CompilerProject
In this project a program was implemented using python that accepts a user's regular expression as input and allows the user to select whether to convert the input to NFA or DFA. 

 

If convert to NFA is selected, the software will output the transition function, First and Final states, as well as the ability to convert the output NFA to DFA.[1] 

The alphabet recognized by this program is: 

* letters [a-z, A-Z] 

* '+' : union 

* '*' : star 

* 'e' : epsilon 

* '()' : grouping 

If Convert Reg to DFA is selected, the program will read the regular expression from the 'input.txt' file and output two images, ast.png and dfa.png. One is of the regex's Abstract Syntax Tree (AST), while the other is of the resulting DFA.[2] 

The alphabet recognized by this program is: 

* letters [a-z, A-Z] 

* '|' : union 

* '*' : star 

* '()' : grouping 
