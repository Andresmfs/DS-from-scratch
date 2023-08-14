# Busca expresiones regulares en un texto y devuelve las líneas que las contienen

import sys
import re

regex = sys.argv[1]

for line in sys.stdin:
    if re.search(regex, line):
        sys.stdout.write(line)
