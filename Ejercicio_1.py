
with open( 'archivo_texto1.txt', 'r') as file:
    lines = file.readlines()  
    cantidad_lineas = len(lines) 

    for line in lines:
           print(line.strip())  
        
    print(f"\nLa cantidad de líneas en el archivo es: {cantidad_lineas}")
