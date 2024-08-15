nombres_a = []
nombres_b = []

with open('archivo_texto3a.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        nombres_a.append(line[:-1])

with open('archivo_texto3b.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        nombres_b.append(line[:-1])

nombres_c = [nombres_a[0] + nombres_b[0], nombres_a[1] + nombres_b[1], nombres_a[2] + nombres_b[2], nombres_a[3] + nombres_b[3]]

print(nombres_c)

with open('archivo_texto3b.txt', 'w+') as file:
    for nombre in nombres_c:
        file.write(nombre + "\n")