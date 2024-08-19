nombres_a = []
nombres_b = []

with open('archivo_texto3a.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        nombres_a.append(line[:-1])
    file.close()

with open('archivo_texto3b.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        nombres_b.append(line[:-1])

with open('archivo_texto3b.txt', 'a') as file:
    contador = 0
    for line in lines:
        file.write("\n"+nombres_a[contador] + nombres_b[contador])
        contador+=1
        