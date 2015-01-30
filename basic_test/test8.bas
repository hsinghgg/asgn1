FOR x = 1 TO 7
CALL GetText NEXT

REM subroutine example
SUB GetText
PRINT "Enter some text:";
INPUT text$
PRINT "The text you entered was: "; text$
END SUB