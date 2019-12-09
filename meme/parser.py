from lark import Lark, InlineTransformer
from pathlib import Path
import os

from .runtime import Symbol


class LispTransformer(InlineTransformer):
    number = float
    name   = str

    def bool(self, term):
        return term == '#t'

    def string(self, string):
        string = string.replace('\\t', '\t').replace('\\"','\"').replace('\\n','\n')[1:-1]
        print("String: ",string)
        return string

    def settext(self,variable,x,y,text):
        return[Symbol('settext'),variable,(x,y),text]

    def setfont(self,fontfamily_path,size):
        return[Symbol('setfont'),fontfamily_path,int(size)]
        
    def save(self,op,variable,name):
        print("OP",op)
        return[Symbol(op),variable,name]

    def symbol(self, symbol):
        return Symbol(symbol)

    def let(self, declarations, expr):
        return [(Symbol('let'),declarations,expr)]

    def attr(self,name,path_or_value):
        return [Symbol('define'),name,path_or_value]

def parse(src: str):
    """
    Compila string de entrada e retorna a S-expression equivalente.
    """
    return parser.parse(src)


def _make_grammar():
    """
    Retorna uma gramática do Lark inicializada.
    """
    path =os.getcwd()+'/meme/grammar.lark'# / 'grammar.lark'
    with open(path) as fd:
        grammar = Lark(fd, parser='lalr', transformer=LispTransformer())
    return grammar

parser = _make_grammar()
