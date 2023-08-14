# Cuenta el número de líneas que recibe de un documento
import sys

count = 0
for line in sys.stdin:
    count += 1

print(count)
