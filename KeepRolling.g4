grammar KeepRolling;

prog: expr
    ;

expr: num
    | lst
    ;

num: INT                                              #num_int
   | lst '!' red_op                                   #num_reduction
   ;

lst: '[' INT (',' INT)* ']'                           #lst_lst
   | INT DICE INT                                     #lst_roll
   | lst map_op num                                   #lst_map
   ;

red_op: OP_ADD | OP_MUL | OP_GRE | OP_LES ;
map_op: OP_ADD | OP_SUB | OP_MUL | OP_DIV | OP_GRE | OP_LES | OP_EQL ;

OP_ADD: '+' ;
OP_SUB: '-' ;
OP_DIV: '/' ;
OP_MUL: '*' ;
OP_GRE: '>' ;
OP_LES: '<' ;
OP_EQL: '=' ;

DICE   : [dDwW] ;
INT    : [0-9]+ ;             // match integers
WS     : [ \t\r\n]+ -> skip ; // toss out whitespaces and tabs
