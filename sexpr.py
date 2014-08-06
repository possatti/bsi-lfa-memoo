''' Parser de S-Expressions.

IMPORTANTE: Nada neste arquivo é meu, o código foi obitido nesse link:
http://rosettacode.org/wiki/S-Expressions#Python , com apenas algumas
modificações minhas. Apesar disso, o link não parece ter qualquer menção
de quem é o verdadeiro autor desse código. Então deixo apenas o link.
'''

import re
 
dbg = False
 
term_regex = r'''(?mx)
    \s*(?:
        (?P<brackl>\()|
        (?P<brackr>\))|
        (?P<num>\-?\d+\.\d+|\-?\d+)|
        (?P<sq>"[^"]*")|
        (?P<s>[^(^)\s]+)
       )'''
 
def parse_sexp(sexp):
    '''Faz o parsing de uma S-Expression.

    O resultado são listas aninhadas que representam os dados.
    '''
    stack = []
    out = []
    if dbg: print("%-6s %-14s %-44s %-s" % tuple("term value out stack".split()))
    for termtypes in re.finditer(term_regex, sexp):
        term, value = [(t,v) for t,v in termtypes.groupdict().items() if v][0]
        if dbg: print("%-7s %-14s %-44r %-r" % (term, value, out, stack))
        if   term == 'brackl':
            stack.append(out)
            out = []
        elif term == 'brackr':
            assert stack, "Trouble with nesting of brackets"
            tmpout, out = out, stack.pop(-1)
            out.append(tmpout)
        elif term == 'num':
            v = float(value)
            if v.is_integer(): v = int(v)
            out.append(v)
        elif term == 'sq':
            out.append(value[1:-1])
        elif term == 's':
            out.append(value)
        else:
            raise NotImplementedError("Error: %r" % (term, value))
    assert not stack, "Trouble with nesting of brackets"
    return out[0]

def print_sexp(exp):
    '''Recebe uma expressão para imprimir no formato de uma S-Expression
    de uma única linha.
    '''
    out = ''
    if type(exp) == type([]):
        out += '(' + ' '.join(print_sexp(x) for x in exp) + ')'
    elif type(exp) == type('') and re.search(r'[\s()]', exp):
        out += '"%s"' % repr(exp)[1:-1].replace('"', '\"')
    else:
        out += '%s' % exp
    return out
 
 
if __name__ == '__main__':
    import sys

    # Lê a S-Expression.
    sexp = sys.stdin.read()
    
    # Imprime a forma crua da expressão.
    print('Input S-expression:\n%s' % sexp)

    # Faz o parsing.
    parsed = parse_sexp(sexp)

    # Imprime a expressão já interpretada.
    print("\nParsed to Python:", parsed)
 
    # Imprime de volta no formato de uma S-Expression.
    print("\nThen back to: '%s'" % print_sexp(parsed))
