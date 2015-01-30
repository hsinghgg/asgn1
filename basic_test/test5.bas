DIM KeyPressed AS STRING

' select case example

CLS


PRINT

PRINT


INPUT "Please Enter A Key (A,B,C,D): ", KeyPressed


KeyPressed = UCASE$(KeyPressed)


PRINT


SELECT CASE KeyPressed

CASE "A"

PRINT "A Was Entered"

CASE "B"

PRINT "B Was Entered"

CASE "C"

PRINT "C Was Entered"

CASE "D"

PRINT "D Was Entered"

CASE ELSE

PRINT "Some Other Key Was Entered"

END SELECT