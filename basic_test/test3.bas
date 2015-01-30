CLS

'if else
PRINT ""
PRINT "Welcome to Jethro's World of Fun, and the like"

INPUT "Please enter in a string: ", mystring$
INPUT "Please enter in a number: ", mynumber

PRINT "You said: ", mystring$
PRINT "You said: ", mynumber
PRINT mynumber, " is a number"
PRINT mystring$, " is a string"

IF INSTR(mystring$, "f") THEN PRINT "There is the letter 'f' in your name!"
IF NOT INSTR(mystring$, "k") THEN PRINT "There is no 'k' in your name!"

IF mynumber > 0 THEN PRINT mynumber; " is bigger than 0"
IF mynumber < 0 THEN PRINT mynumber; " is smaller than 0"
IF mynumber = 0 THEN PRINT mynumber; " is equal to 0"

IF INSTR(mystring$, " ") AND mynumber > 0 THEN PRINT "There is a space in your phrase AND your number is bigger than 0!"
IF INSTR(mystring$, " ") OR mynumber > 0 THEN PRINT "There is a space in your phrase OR your number is bigger than 0!"

PRINT ""
PRINT "Please press a key to continue..."
SLEEP

