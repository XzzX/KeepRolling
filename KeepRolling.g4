grammar KeepRolling;

prog: stat+ 
    ;

stat: expr NEWLINE        #print_expr
    ;

expr: datum                    #expr_datum
    | datum '!' (OP_PLUS | OP_GREATER | OP_LESS)   #expr_reduction
    ;

datum: INT                #datum_int
     | int_list           #datum_list
     | roll               #datum_roll
     ;

int_list: '[' INT (',' INT)* ']'
        ;

roll: INT DICE INT
    ;

OP_PLUS: '+' ;
OP_GREATER: '>' ;
OP_LESS: '<' ;

DICE   : [dDwW] ;
INT    : [0-9]+ ;         // match integers
NEWLINE: '\r'? '\n' ;     // return newlines to parser (is end-statement signal)
WS     : [ \t]+ -> skip ; // toss out whitespace
