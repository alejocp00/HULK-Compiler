from src.syntax_analysis.grammLR1 import *


def build_regex():

    return [
        (number, "(\-|\+)?(0|[1-9][0-9]*)(\.[0-9]+)?([eE][\+\-]?[0-9]+)?"),
        ("space", "( )*|\n|\t"),
        (Equal, "="),
        (Destroy, ":="),
        (Colon, ":"),
        (Arrow, "=>"),
        (Less, "<"),
        (LessEqual, "<="),
        (Greater, ">"),
        (GreaterEqual, ">="),
        (CompEqual, "=="),
        (NotEqual, "!="),
        (Print, "print"),
        (If, "if"),
        (Elif, "elif"),
        (Else, "else"),
        (Let, "let"),
        (In, "in"),
        (For, "for"),
        (While, "while"),
        (Function, "function"),
        (Type, "type"),
        (Inherits, "inherits"),
        (New, "new"),
        (arroba, "@"),
        # (sqrt, "sqrt"),
        # (sin, "sin"),
        # (cos, "cos"),
        # (tan, "tan"),
        # (exp, "exp"),
        # (log, "log"),
        # (rand, "rand"),
        (And, "and"),
        (Or, "or"),
        (Not, "not"),
        (True_, "true"),
        (False_, "false"),
        (Is, "is"),
        (PI, "PI"),
        (identifier, "[a-zA-Z_][a-zA-Z0-9_]*"),
        (
            string,
            '"([^"])*"',
        ),
        (Dot, "\."),
        (oBrace, "\{"),
        (cBrace, "\}"),
        (Plus, "\+"),
        (Minus, "\-"),
        (Mult, "\*"),
        (Div, "\/"),
        (Pow, "(\^|\**)"),
        (Mod, "%"),
        (oPar, "\("),
        (cPar, "\)"),
        (Semi, ";"),
        (Comma, ","),
    ]
