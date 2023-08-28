def metodo_kleene(palabras, nivel):
    if nivel == 0:
        return [""]
    elif nivel == 1:
        return palabras
    else:
        resultado = palabras[:]
        for palabra in palabras:
            for p in metodo_kleene(palabras, nivel - 1):
                nueva_palabra = palabra + p
                if nueva_palabra not in resultado:
                    resultado.append(nueva_palabra)
        return resultado

def main():
    num_palabras = int(input("¿Cuántas palabras contiene el lenguaje? "))
    lenguaje = []
    for i in range(num_palabras):
        palabra = input(f"Ingresa la palabra {i + 1} del lenguaje: ")
        lenguaje.append(palabra)
    
    nivel = int(input("¿Qué nivel de cerradura de Kleene deseas conocer? "))
    
    palabras_resultado = metodo_kleene(lenguaje, nivel)
    
    print("\nPalabras correspondientes al nivel de cerradura:")
    for palabra in palabras_resultado:
        print(palabra)
    
    print(f"\nCantidad de palabras generadas para el nivel {nivel}: {len(palabras_resultado)}")

if __name__ == "__main__":
    main()