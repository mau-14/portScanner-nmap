import nmap

# Para el figlet
import os
# Biblioteca estándar de python para las expresiones regulares
import re

# Expresión regular para reconocer IPv4 addresses
ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

# Expresión regular para extraer los puertos que quieres escanear
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

port_min = 0
port_max = 65535

os.system("figlet Mauri")

print("\n****************************************************************")
print("\n* https://github.com/mau-14                                    *")
print("\n****************************************************************")

open_ports = []

while True:
    ip_add_entered = input("\nPor favor introduce la ip que quieres escanear: ")
    if ip_add_pattern.search(ip_add_entered):
        print(f"{ip_add_entered} es una ip válida")
        break


while True:
     # Se pueden escanear 65535 puertos así que no se recomienda escanearlos todos 
    print("Por favor introduzca el rango de puertos que quieres escanear en este formato: <int>-<int> (ejemplo 80-100)")
    port_range = input("Introduce puertos: ")
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break


nm = nmap.PortScanner()

for port in range(port_min, port_max + 1):
    try:

        result = nm.scan(ip_add_entered, str(port))
        # Este print es para ver lo que devuelve el scan del nmap
        # print(result)

        port_status = (result['scan'][ip_add_entered]['tcp'][port]['state'])
        print(f"Puerto {port} es {port_status}")

    except:
        
        print(f"No se puedo escanear el puerto {port}.")

