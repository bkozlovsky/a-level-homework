import sys
from pygments.lexers import guess_lexer, guess_lexer_for_filename
from pygments import highlight
from pygments.formatters import TerminalTrueColorFormatter

for i in range(1, len(sys.argv)):
    f = open(sys.argv[i], "r")
    code = f.read()
    try:
        lexer = guess_lexer(code)
    except TypeError:
        lexer = TextLexer()
    print(highlight(code, lexer, TerminalTrueColorFormatter()))
    f.close()
