import ply.lex as lex
import sys
import re
reserved = {

   'PRINT' : 'KEYWORD_PRINT',
   'END' : 'KEYWORD_END',
   'CLS' : 'KEYWORD_CLS',
   'LET' : 'KEYWORD_LET',
   'BEGIN' : 'KEYWORD_BEGIN',
   'DATA' : 'KEYWORD_DATA',
   'IF' : 'KEYWORD_IF',
   'NOT' : 'KEYWORD_NOT',
   'THEN' : 'KEYWORD_THEN',
   'ELSE' : 'KEYWORD_ELSE',
   'ELSEIF' : 'KEYWORD_ELSEIF',
   'STEP' : 'KEYWORD_STEP',
   'LOOP' : 'KEYWORD_LOOP',
   'CALL' : 'KEYWORD_CALL',   
   # 'END IF' : 'KEYWORD_END_IF',#SPACE
   'FOR' : 'KEYWORD_FOR',
   'TO' : 'KEYWORD_TO',
   'NEXT' : 'KEYWORD_NEXT',
   'WHILE' : 'KEYWORD_WHILE',
   'WEND' : 'KEYWORD_WEND',
   'REPEAT' : 'KEYWORD_REPEAT',
   'UNTIL' : 'KEYWORD_UNTIL',
   'DO' : 'KEYWORD_DO',
   'GOTO' : 'KEYWORD_GOTO',
   'GOSUB' : 'KEYWORD_GOSUB',
   'ON' : 'KEYWORD_ON',
   'INPUT' : 'KEYWORD_INPUT',
   'TAB' : 'KEYWORD_TAB',
   'AT' : 'KEYWORD_AT',
   'USR' : 'KEYWORD_USR',
   'TRON' : 'KEYWORD_TRON',
   'TROFF' : 'KEYWORD_TROFF',
   'SLEEP' : 'KEYWORD_SLEEP',
   'SELECT' : 'KEYWORD_SELECT', #######
   'CASE' : 'KEYWORD_CASE',
   'DECLARE' : 'KEYWORD_DECLARE',
   'SUB' : 'KEYWORD_SUB',
   'FUNCTION' : 'KEYWORD_FUNCTION',
   # 'CLS' : 'KEYWORD_END_FUNCTION',#SPACE
   'DELAY' : 'KEYWORD_DELAY',
   'SHELL' : 'KEYWORD_SHELL',
   'READ' : 'KEYWORD_READ',
   'RND' : 'KEYWORD_RND',
   'RANDOMIZE' : 'KEYWORD_RANDOMIZE',
   'TYPE' : 'KEYWORD_TYPE',
   'CONST' : 'KEYWORD_CONST',
   # 'CLS' : 'KEYWORD_END_TYPE',
   'AS' : 'KEYWORD_AS',
   'INTEGER': 'KEYWORD_INTEGER',#%
   'STRING': 'KEYWORD_STRING',#$, (.S)
   'LONG': 'KEYWORD_LONG',#&
   'SINGLE': 'KEYWORD_SINGLE',#!
   'DOUBLE': 'KEYWORD_DOUBLE',
   'DIM' : 'KEYWORD_DIM',
   'REDIM' : 'KEYWORD_REDIM',
   'STOP' : 'KEYWORD_STOP', #STOP EXECUTION OF PROGRAM
   'DELETE' : 'KEYWORD_DELETE', #######
   'AND' : 'OPERATOR_AND',
   'OR' : 'OPERATOR_OR',
   'SQR' : 'OPERATOR_SQR',
   'SQ' : 'OPERATOR_SQ',  #SQUARE ROOT
   'MOD' : 'OPERATOR_MOD',
   'ABS' : 'OPERATOR_ABS',
   'SIN' : 'OPERATOR_SIN',
   'COS' : 'OPERATOR_COS',
   'TAN' : 'OPERATOR_TAN',
   'ATN' : 'OPERATOR_ATN',  #Calculate pi to accuracy (pi=ATN(1)*4) arctangent, inverse tangent
   'LOG' : 'OPERATOR_LOG',
   'EXP' : 'OPERATOR_EXP',
   'INT' : 'OPERATOR_INT',  #FLOOR  
   'FIX' : 'OPERATOR_FIX',  #INTEGRAL PART RETURNED
   'CINT' : 'OPERATOR_CINT',  #NUMERIC ROUNDING FOR INTEGERS
   'CLNG' : 'OPERATOR_CLNG',  #NUMERIC ROUNDING FOR LONG INTEGERS
   'CSNG' : 'OPERATOR_CSNG',  #CONVERTS TO SINGAL PRECISION
   'CDBL' : 'OPERATOR_CDBL',  #CONVERTS TO DOUBLE PRECISION
   'LEN' : 'OPERATOR_LEN',  #STRING LENGTH
   'VAL' : 'OPERATOR_VAL', #EXTRACTS NUMBER FROM STRING
   'ASC' : 'OPERATOR_ASC',  #ASCII CODE
   'INSTR' : 'OPERATOR_INSTR',  #STRING SEARCH FUNCTION
   'SGN' : 'OPERATOR_SGN'

}

# List of token names
tokens = [

   'KEYWORD_END_IF', #TODO #SPACE
   'KEYWORD_END_FUNCTION', #TODO #SPACE
   'KEYWORD_END_TYPE', #TODO #SPACE

   'OPERATOR_POWER',
   'OPERATOR_EQUAL',
   'OPERATOR_NOTEQUAL',
   'OPERATOR_LESSTHAN',
   'OPERATOR_LESSTHANEQUAL',
   'OPERATOR_GREATERTHAN',
   'OPERATOR_GREATERTHANEQUAL',
   'OPERATOR_ADD',
   'OPERATOR_SUBTRACT',
   'OPERATOR_TIMES',
   'OPERATOR_DIVIDE',
   'OPERATOR_EQUALTO',
   
   'TYPE_INTEGER',#%
   'TYPE_STRING',#$, (.S)
   'TYPE_LONG',#&
   'TYPE_SINGLE',#!
   'TYPE_DOUBLE',##

   'LPAREN',
   'RPAREN',
   'SEMICOLON',
   'COLON',
   'COMMA',
   'COMMENT', #TODO

   # 'LINE_LABEL',
   # 'LINE_NUMBER',

   'IDENTIFIER',

   'CONSTANT_INTEGER',
   'CONSTANT_STRING',
   'CONSTANT_FLOAT'
] + list(reserved.values())

# Regular expression rules for simple tokens

t_LPAREN  = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_COLON = r':'
t_COMMA = r','
t_OPERATOR_ADD = r'\+'
t_OPERATOR_SUBTRACT = r'-'
t_OPERATOR_TIMES = r'\*'
t_OPERATOR_DIVIDE = r'/'
t_OPERATOR_POWER = r'\^'
t_OPERATOR_EQUAL = r'=='
t_OPERATOR_NOTEQUAL = r'<>'
t_OPERATOR_LESSTHANEQUAL = r'<='
t_OPERATOR_GREATERTHANEQUAL = r'>='
t_OPERATOR_LESSTHAN = r'<'
t_OPERATOR_GREATERTHAN = r'>'
t_OPERATOR_EQUALTO = r'=' #can be assignment or comparison depending on context
t_CONSTANT_STRING = r'"[A-Za-z0-9_\.\t\+\ ~!@$\-%^&*()\'<>{}\?\[\];\:\/\\\|,`=#]*"'

# p = re.compile("ab*", re.IGNORECASE)
# if(p.match("a")): print "yes"
# if(p.match("Abb")): print "gtf"


def t_COMMENT(t):
    r'((\') | ((R|r)(E|e)(m|M)(\ |\t)))[A-Za-z0-9_\.\t\+\ ~!@$,\-%^&*()\'\?<>{}\[\]\:;\/\\\|`=#]*'
    return t

def t_CONSTANT_FLOAT(t):    ##PARSER INT -> FLOAT
    r'-?\d+\.\d+'
    t.value = float(t.value)    
    return t


def t_CONSTANT_INTEGER(t):
    r'-?\d+'
    t.value = int(t.value)    
    return t

def t_TYPE_STRING(t):
    r'[A-Za-z][A-Za-z0-9_\.]*\$'
    t.type = reserved.get(t.value,'TYPE_STRING')    
    return t

def t_TYPE_DOUBLE(t):
    r'[A-Za-z][A-Za-z0-9_\.]*\#'
    t.type = reserved.get(t.value,'TYPE_DOUBLE')    
    return t

def t_TYPE_SINGLE(t):
    r'[A-Za-z][A-Za-z0-9_\.]*\!'
    t.type = reserved.get(t.value,'TYPE_SINGLE')    
    return t

def t_TYPE_LONG(t):
    r'[A-Za-z][A-Za-z0-9_\.]*\&'
    t.type = reserved.get(t.value,'TYPE_LONG')    
    return t

def t_TYPE_INTEGER(t):
    r'[A-Za-z][A-Za-z0-9_\.]*\%'
    t.type = reserved.get(t.value,'TYPE_INTEGER')    
    return t

def t_IDENTIFIER(t):
    r'[A-Za-z][A-Za-z0-9_\.]*'
    t.type = reserved.get(t.value,'IDENTIFIER')    
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "REM ERROR: Illegal character '%s'" % t.value[0]
    flag = 0
    t.lexer.skip(1)

# Build the lexer
try:
  lexer = lex.lex(reflags = re.I)
except IOError, e:
  import errno
  if e.errno != errno.EACCES:
    raise

filename = sys.argv[-1]
data = open(filename, 'r')
# outputfile = open('lexer_output.txt', 'w')
# outputfile.truncate()

while True:
  ndata = data.readline()
  if not ndata: break
  print(ndata.rstrip('\n'))
  # outputfile.write(ndata.rstrip('\n'))
  data_upper = ndata.upper()
  lexer.input(data_upper)
# Tokenize
  string1 = "REM "  
  while True:
      flag = 1
      tok = lexer.token()
      if not tok: break   
      
      if tok.value == "END":
        tok1 = lexer.token()
        if not tok1:
          string1 += tok.type
          string1 += " " 
          break   
        elif tok1.value == "IF":
          tok.value = "END IF"
          tok.type = "KEYWORD_END_IF"
          string1 += tok.type
          string1 += " " 
        elif tok1.value == "FUNCTION":
          tok.value = "END FUNCTION"
          tok.type = "KEYWORD_END_FUNCTION"
          string1 += tok.type
          string1 += " " 
          # print tok
        elif tok1.value == "TYPE":
          tok.value = "END TYPE"
          tok.type = "KEYWORD_END_TYPE"
          string1 += tok.type
          string1 += " " 
        elif tok1.value == "SELECT":
          tok.value = "END SELECT"
          tok.type = "KEYWORD_END_SELECT"
          string1 += tok.type
          string1 += " " 
        elif tok1.value == "SUB":
          tok.value = "END SUB"
          tok.type = "KEYWORD_END_SUB"
          string1 += tok.type
          string1 += " " 
          # print tok
        else: 
          string1 += tok.type
          string1 += " " 
          string1 += tok1.type
          string1 += " "
          # print tok
          # print tok1
      
      elif tok.value == "SELECT":
        tok1 = lexer.token()
        if not tok1:
          string1 += tok.type
          string1 += " " 
          break   
        elif tok1.value == "CASE":
          tok.value = "SELECT CASE "
          tok.type = "KEYWORD_SELECT_CASE"
          string1 += tok.type
          string1 += " " 
        else: 
          string1 += tok.type
          string1 += " " 
          string1 += tok1.type
          string1 += " "


      elif tok.value == "CASE":
        tok1 = lexer.token()
        if not tok1:
          string1 += tok.type
          string1 += " " 
          break   
        elif tok1.value == "ELSE":
          tok.value = "CASE ELSE"
          tok.type = "KEYWORD_CASE_ELSE"
          string1 += tok.type
          string1 += " " 
        else: 
          string1 += tok.type
          string1 += " " 
          string1 += tok1.type
          string1 += " "
      
      else: 
        string1 += tok.type
        string1 += " " 

  # string1 += "\n"
  if(string1 != "REM "):
    print(string1)
    # outputfile.write(string1)

