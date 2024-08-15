with open("archivo1.txt", "r") as archivo1:
    texto = archivo1.read()

    with open("archivo2.txt", 'w') as archivo2:
        archivo2.write(texto)