
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BEGIN DIV DONE ELSE EQ EQEQ FLING FOR GE GT ID IF INCREASE LE LPAREN LT MEK MINUS MUL NEQ NUMBER PLUS RPAREN SET STRING TOprogram : BEGIN stmt_list DONEstmt_list : stmt stmt_list\n| stmt : assignment\n| print_stmt\n| if_stmt\n| for_loop\n| natural_stmtassignment : MEK ID EQ exprprint_stmt : FLING LPAREN STRING RPAREN\n| FLING LPAREN expr RPARENif_stmt : IF expr BEGIN stmt_list DONE\n| IF expr BEGIN stmt_list DONE ELSE BEGIN stmt_list DONEfor_loop : FOR ID EQ expr TO expr BEGIN stmt_list DONEnatural_stmt : SET ID TO exprexpr : expr PLUS expr\n| expr MINUS expr\n| expr MUL expr\n| expr DIV expr\n| expr GT expr\n| expr LT expr\n| expr GE expr\n| expr LE expr\n| expr EQEQ expr\n| expr NEQ exprexpr : LPAREN expr RPARENexpr : NUMBERexpr : STRINGexpr : ID'
    
_lr_action_items = {'BEGIN':([0,19,21,22,23,47,48,49,50,51,52,53,54,55,56,57,62,63,],[2,29,-27,-28,-29,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,64,65,]),'$end':([1,15,],[0,-1,]),'DONE':([2,3,4,5,6,7,8,9,16,21,22,23,29,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,59,60,64,65,66,67,68,69,],[-3,15,-3,-4,-5,-6,-7,-8,-2,-27,-28,-29,-3,-9,-10,-11,60,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-15,-12,-3,-3,68,69,-13,-14,]),'MEK':([2,4,5,6,7,8,9,21,22,23,29,43,44,45,47,48,49,50,51,52,53,54,55,56,57,59,60,64,65,68,69,],[10,10,-4,-5,-6,-7,-8,-27,-28,-29,10,-9,-10,-11,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-15,-12,10,10,-13,-14,]),'FLING':([2,4,5,6,7,8,9,21,22,23,29,43,44,45,47,48,49,50,51,52,53,54,55,56,57,59,60,64,65,68,69,],[11,11,-4,-5,-6,-7,-8,-27,-28,-29,11,-9,-10,-11,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-15,-12,11,11,-13,-14,]),'IF':([2,4,5,6,7,8,9,21,22,23,29,43,44,45,47,48,49,50,51,52,53,54,55,56,57,59,60,64,65,68,69,],[12,12,-4,-5,-6,-7,-8,-27,-28,-29,12,-9,-10,-11,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-15,-12,12,12,-13,-14,]),'FOR':([2,4,5,6,7,8,9,21,22,23,29,43,44,45,47,48,49,50,51,52,53,54,55,56,57,59,60,64,65,68,69,],[13,13,-4,-5,-6,-7,-8,-27,-28,-29,13,-9,-10,-11,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-15,-12,13,13,-13,-14,]),'SET':([2,4,5,6,7,8,9,21,22,23,29,43,44,45,47,48,49,50,51,52,53,54,55,56,57,59,60,64,65,68,69,],[14,14,-4,-5,-6,-7,-8,-27,-28,-29,14,-9,-10,-11,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-15,-12,14,14,-13,-14,]),'ID':([10,12,13,14,18,20,26,30,31,32,33,34,35,36,37,38,39,41,42,61,],[17,23,24,25,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'LPAREN':([11,12,18,20,26,30,31,32,33,34,35,36,37,38,39,41,42,61,],[18,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'NUMBER':([12,18,20,26,30,31,32,33,34,35,36,37,38,39,41,42,61,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'STRING':([12,18,20,26,30,31,32,33,34,35,36,37,38,39,41,42,61,],[22,27,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'EQ':([17,24,],[26,41,]),'PLUS':([19,21,22,23,27,28,40,43,47,48,49,50,51,52,53,54,55,56,57,58,59,63,],[30,-27,-28,-29,-28,30,30,30,30,30,30,30,30,30,30,30,30,30,-26,30,30,30,]),'MINUS':([19,21,22,23,27,28,40,43,47,48,49,50,51,52,53,54,55,56,57,58,59,63,],[31,-27,-28,-29,-28,31,31,31,31,31,31,31,31,31,31,31,31,31,-26,31,31,31,]),'MUL':([19,21,22,23,27,28,40,43,47,48,49,50,51,52,53,54,55,56,57,58,59,63,],[32,-27,-28,-29,-28,32,32,32,32,32,32,32,32,32,32,32,32,32,-26,32,32,32,]),'DIV':([19,21,22,23,27,28,40,43,47,48,49,50,51,52,53,54,55,56,57,58,59,63,],[33,-27,-28,-29,-28,33,33,33,33,33,33,33,33,33,33,33,33,33,-26,33,33,33,]),'GT':([19,21,22,23,27,28,40,43,47,48,49,50,51,52,53,54,55,56,57,58,59,63,],[34,-27,-28,-29,-28,34,34,34,34,34,34,34,34,34,34,34,34,34,-26,34,34,34,]),'LT':([19,21,22,23,27,28,40,43,47,48,49,50,51,52,53,54,55,56,57,58,59,63,],[35,-27,-28,-29,-28,35,35,35,35,35,35,35,35,35,35,35,35,35,-26,35,35,35,]),'GE':([19,21,22,23,27,28,40,43,47,48,49,50,51,52,53,54,55,56,57,58,59,63,],[36,-27,-28,-29,-28,36,36,36,36,36,36,36,36,36,36,36,36,36,-26,36,36,36,]),'LE':([19,21,22,23,27,28,40,43,47,48,49,50,51,52,53,54,55,56,57,58,59,63,],[37,-27,-28,-29,-28,37,37,37,37,37,37,37,37,37,37,37,37,37,-26,37,37,37,]),'EQEQ':([19,21,22,23,27,28,40,43,47,48,49,50,51,52,53,54,55,56,57,58,59,63,],[38,-27,-28,-29,-28,38,38,38,38,38,38,38,38,38,38,38,38,38,-26,38,38,38,]),'NEQ':([19,21,22,23,27,28,40,43,47,48,49,50,51,52,53,54,55,56,57,58,59,63,],[39,-27,-28,-29,-28,39,39,39,39,39,39,39,39,39,39,39,39,39,-26,39,39,39,]),'RPAREN':([21,22,23,27,28,40,47,48,49,50,51,52,53,54,55,56,57,],[-27,-28,-29,44,45,57,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,]),'TO':([21,22,23,25,47,48,49,50,51,52,53,54,55,56,57,58,],[-27,-28,-29,42,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,61,]),'ELSE':([60,],[62,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'stmt_list':([2,4,29,64,65,],[3,16,46,66,67,]),'stmt':([2,4,29,64,65,],[4,4,4,4,4,]),'assignment':([2,4,29,64,65,],[5,5,5,5,5,]),'print_stmt':([2,4,29,64,65,],[6,6,6,6,6,]),'if_stmt':([2,4,29,64,65,],[7,7,7,7,7,]),'for_loop':([2,4,29,64,65,],[8,8,8,8,8,]),'natural_stmt':([2,4,29,64,65,],[9,9,9,9,9,]),'expr':([12,18,20,26,30,31,32,33,34,35,36,37,38,39,41,42,61,],[19,28,40,43,47,48,49,50,51,52,53,54,55,56,58,59,63,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> BEGIN stmt_list DONE','program',3,'p_program','simplipyja_parser.py',6),
  ('stmt_list -> stmt stmt_list','stmt_list',2,'p_stmt_list','simplipyja_parser.py',11),
  ('stmt_list -> <empty>','stmt_list',0,'p_stmt_list','simplipyja_parser.py',12),
  ('stmt -> assignment','stmt',1,'p_stmt','simplipyja_parser.py',16),
  ('stmt -> print_stmt','stmt',1,'p_stmt','simplipyja_parser.py',17),
  ('stmt -> if_stmt','stmt',1,'p_stmt','simplipyja_parser.py',18),
  ('stmt -> for_loop','stmt',1,'p_stmt','simplipyja_parser.py',19),
  ('stmt -> natural_stmt','stmt',1,'p_stmt','simplipyja_parser.py',20),
  ('assignment -> MEK ID EQ expr','assignment',4,'p_assignment','simplipyja_parser.py',24),
  ('print_stmt -> FLING LPAREN STRING RPAREN','print_stmt',4,'p_print_stmt','simplipyja_parser.py',28),
  ('print_stmt -> FLING LPAREN expr RPAREN','print_stmt',4,'p_print_stmt','simplipyja_parser.py',29),
  ('if_stmt -> IF expr BEGIN stmt_list DONE','if_stmt',5,'p_if_stmt','simplipyja_parser.py',33),
  ('if_stmt -> IF expr BEGIN stmt_list DONE ELSE BEGIN stmt_list DONE','if_stmt',9,'p_if_stmt','simplipyja_parser.py',34),
  ('for_loop -> FOR ID EQ expr TO expr BEGIN stmt_list DONE','for_loop',9,'p_for_loop','simplipyja_parser.py',41),
  ('natural_stmt -> SET ID TO expr','natural_stmt',4,'p_natural_stmt','simplipyja_parser.py',45),
  ('expr -> expr PLUS expr','expr',3,'p_expr_binop','simplipyja_parser.py',49),
  ('expr -> expr MINUS expr','expr',3,'p_expr_binop','simplipyja_parser.py',50),
  ('expr -> expr MUL expr','expr',3,'p_expr_binop','simplipyja_parser.py',51),
  ('expr -> expr DIV expr','expr',3,'p_expr_binop','simplipyja_parser.py',52),
  ('expr -> expr GT expr','expr',3,'p_expr_binop','simplipyja_parser.py',53),
  ('expr -> expr LT expr','expr',3,'p_expr_binop','simplipyja_parser.py',54),
  ('expr -> expr GE expr','expr',3,'p_expr_binop','simplipyja_parser.py',55),
  ('expr -> expr LE expr','expr',3,'p_expr_binop','simplipyja_parser.py',56),
  ('expr -> expr EQEQ expr','expr',3,'p_expr_binop','simplipyja_parser.py',57),
  ('expr -> expr NEQ expr','expr',3,'p_expr_binop','simplipyja_parser.py',58),
  ('expr -> LPAREN expr RPAREN','expr',3,'p_expr_group','simplipyja_parser.py',62),
  ('expr -> NUMBER','expr',1,'p_expr_number','simplipyja_parser.py',66),
  ('expr -> STRING','expr',1,'p_expr_string','simplipyja_parser.py',70),
  ('expr -> ID','expr',1,'p_expr_id','simplipyja_parser.py',74),
]
