# Cuenta el número de dominios diferentes de un archivo con direcciones de correo electrónico y crea un histograma

import csv
from collections import Counter
import matplotlib.pyplot as plt


def get_domain(email_adress: str) -> str:
    """Separa en @ y devuelve la última parte"""
    return email_adress.lower().split('@')[-1]


assert get_domain('andres@midominio.com') == 'midominio.com'


with open('./obtener_datos/emails.txt', 'r', encoding='utf-8') as f:
    domain_counts = Counter(get_domain(line.strip())
                            for line in f if "@" in line)

domains = domain_counts.keys()
plt.bar(domains, domain_counts.values())
plt.xticks(range(len(domains)), domains)
plt.yticks(range(max(domain_counts.values()) + 1))
# plt.show()

with open('./obtener_datos/tab_delimited.txt', 'w') as f:
    f.write(f"""6/20/2014\tAAPL\t90.91
6/20/2014\tMSFT\t41.68
6/20/2014\tFB\t64.5
6/19/2014\tAAPL\t91.86
6/19/2014\tMSFT\t41.51
6/19/2014\tFB\t64.34
""")


with open('./obtener_datos/tab_delimited.txt', 'r') as f:
    tab_reader = csv.reader(f, delimiter='\t')
    dates = []
    symbols = []
    for row in tab_reader:
        date = row[0]
        symbol = row[1]
        closing_price = float(row[2])
        dates.append(date)
        symbols.append(symbol)
