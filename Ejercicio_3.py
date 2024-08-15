with open('archivo_texto3a.txt', 'r+') as file:
    lines = file.readlines()
    for line in lines:
        nombres_a = [line.strip("\n")]

print(nombres_a)
