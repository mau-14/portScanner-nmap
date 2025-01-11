import nmap

# Para el figlet
import os
# Biblioteca estándar de python para las expresiones regulares
import re

# Expresión regular para reconocer IPv4 addresses
ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1.3}$")

# Expresión regular para extraer los puertos que quieres escanear
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

port_min = 0
port_max = 65535

os.system("figlet Mauri")

print("\n****************************************************************")
print("\n* https://github.com/mau-14                                    *")
print("\n****************************************************************")


