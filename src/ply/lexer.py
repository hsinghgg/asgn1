import ply.lex as lex 

reserved = {

#turbo pascal
    'absolute' : 'ABSOLUTE',
    'and' : 'AND',
    'array' : 'ARRAY',
    'asm'   : 'ASM',
    'begin' : 'BEGIN',
    'case'  : 'CASE',
    'char' : 'CHAR',
    'clrscr' : 'CLRSCR',
    'const' : 'CONST',
    'constructor' : 'CONSTRUCTOR',
    'delay' : 'DELAY',
    'destructor' : 'DESTRUCTOR',
    'div' : 'DIV',
    'do' : 'DO',
    'downto' : 'DOWNTO',
    'else' : 'ELSE',
    'end' : 'END',
    'file' : 'FILE',
    'for' : 'FOR',
    'function' : 'FUNCTION',
    'gotoXy' : 'GOTOXY',
    'goto' : 'GOTO',
    'halt' : 'HALT',
    'if' : 'IF',
    'implementation' : 'IMPLEMENTATION',
    'in' : 'IN',
    'inherited' : 'INHERITED',
    'inline' : 'INLINE',
    'interface' : 'INTERFACE',
    'label' : 'LABEL',
    'mod' : 'MOD',
    'nil' : 'NIL',
    'not' : 'NOT',
    'object' : 'OBJECT',
    'of' : 'OF',
    'on' : 'ON',
    'operator' : 'OPERATOR',
    'or' : 'OR',
    'packed' : 'PACKED',
    'procedure' : 'PROCEDURE',
    'program' : 'PROGRAM',
    'record' : 'RECORD',
    'reintroduce' : 'REINTRODUCE',
    'repeat' : 'REPEAT',
    'self' : 'SELF',
    'set' : 'SET',
    'shl' : 'SHL',
    'shr' : 'SHR',
    'string' : 'STRING',
    'then' : 'THEN',
    'to' : 'TO',
    'type' : 'TYPE',
    'unit' : 'UNIT',
    'until' : 'UNTIL',
    'uses' : 'USES',
    'var' : 'VAR',
    'while' : 'WHILE',
    'writeln' : 'WRITELN',
    'write' : 'WRITE',
    'readln' : 'READLN',
    'read' : 'READ',
    'readkey' : 'READKEY',
    'textbackgraound' : 'TEXTBACKGROUND',
    'textcolor' : 'TEXTCOLOR',
    'with' : 'WITH',
    'var' : 'VAR',
    'xor' : 'XOR',

# free pascal
    'dispose' : 'DISPOSE',
    'exit' : 'EXIT',
    'false' : 'FALSE',
    'new' : 'NEW',
    'true' : 'TRUE',


#object pascal
    'as' : 'AS',
    'class' : 'CLASS',
    'dispinterface' : 'DISPINTERFACE',
    'except' : 'EXCEPT',
    'exports' : 'EXPORTS',
    'finalization' : 'FINALIZATION',
    'finally' : 'FINALLY',
    'initialization' : 'INITIALIZATION',
    'inline' : 'INLINE',
    'is' : 'IS',
    'library' : 'LIBRARY',
    'on' : 'ON',
    'out' : 'OUT',
    'packed' : 'PACKED',
    'property' : 'PROPERTY',
    'raise' : 'RAISE',
    'resourcestring' : 'RESOURCESTRING',
    'threadvar' : 'THREADVAR',
    'try' : 'TRY',
}








tokens = list(reserved.values()) + [

#literals
'SSTRING','ID','INTEGER','FLOAT', 

#operators
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'STST','GL','LG','HASH','CARET','DOLLAR','DVDV',
    'LSHIFT', 'RSHIFT','ATR',
    'LT', 'LE', 'GT', 'GE', 

# Assignment (=, *=, /=, %=, +=, -=, <<=, >>=, &=, ^=, |=)
    'EQUALS','ASSIGN', 'TIMESEQUAL', 'DIVEQUAL', 'PLUSEQUAL', 
    'MINUSEQUAL', 



# Delimeters ( ) [ ] { } , . ; :
    'LPAREN', 'RPAREN',
    'LBRACKET', 'RBRACKET',
    'LBRACE', 'RBRACE',
    'COMMA', 'PERIOD', 'SEMI', 'COLON',

]
	



# Operators
t_PLUS             = r'\+'
t_MINUS            = r'-'
t_TIMES            = r'\*'
t_DIVIDE           = r'/'
t_LSHIFT           = r'\<\<'
t_RSHIFT           = r'\>\>'
t_ATR              = r'\@'
t_DOLLAR           = r'\$'
t_HASH             = r'\#'
t_CARET            = r'\^'
t_LT               = r'<'
t_LG               = r'<>'
t_GL               = r'><'
t_DVDV             = r'//'
t_STST             = r'\*\*'
t_GT               = r'>'
t_LE               = r'<='
t_GE               = r'>='



# Assignment operators

t_EQUALS           = r'='
t_ASSIGN           = r':='
t_TIMESEQUAL       = r'\*='
t_DIVEQUAL         = r'/='
t_PLUSEQUAL        = r'\+='
t_MINUSEQUAL       = r'-='





# Delimeters
t_LPAREN           = r'\('
t_RPAREN           = r'\)'
t_LBRACKET         = r'\['
t_RBRACKET         = r'\]'
t_LBRACE           = r'\{'
t_RBRACE           = r'\}'
t_COMMA            = r'\,'
t_PERIOD           = r'\.'
t_SEMI             = r'\;'
t_COLON            = r'\:'

#string
t_SSTRING           = r'\'([^\\\n]|(\\.))*?\''


#integer
t_INTEGER = r'\d+ | \$[0-9A-Fa-f]+ | &[0-7]+ | %[0-1]+'

#float
t_FLOAT = r'((\d+)(\.\d+)(E(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'



#ignoring comment
def t_COMMENT(t):
    r'//(.*) | \{[^\{\}]*\} | \(\*[^"(*""*)"]*\*\)'
    pass


#checking for identifier
def t_ID(t):
    r'[A-Za-z_][\w_]*'
    t.type = reserved.get(t.value.lower(),"ID")
    return t

#computing line number
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


#computing column number though not necessary
def find_column(input,token):
    last_cr = input.rfind('\n',0,token.lexpos)
    if last_cr < 0:
        last_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column

#ignoring blank space
t_ignore = ' \t'

#raising error code
def t_error(t):
    print "Illegal character '%s'" %t.value[0]
    t.lexer.skip(1)

#building lex
lexer = lex.lex()

data = '''
#for
while
a3 + 4 * 10
library
'bla bla'
Asm
asm
read
set
Readln
Readjunk
$23E
&067
#65
%000111
2.3E-17
//c
{c{ab}}
(*a*) c*)
 + -20 *2
'c'

PrograM expressionTest (input, output);
 var a, b : integer;
        c : real;
 BeGIn
   a := 3;
   b := a * 4;
   c := (b + a)/ 2
 End.

'''

lexer.input(data)


#while True:
#    tok = lexer.token()
#    if not tok: break
#    print tok


for tok in lexer:
    print tok


