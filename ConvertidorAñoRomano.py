# Clase para convertir años a números romanos
class ConvertidorAñoRomano:
    def __init__(self):
        # Lista de tuplas (valor, símbolo) para la conversión
        # Ordenada de mayor a menor para facilitar la conversión
        self.valores = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

    def convertir(self, numero):
        # Validación de entrada
        if not isinstance(numero, int) or numero < 1 or numero > 3999:
            raise ValueError("El año debe ser un número entre 1 y 3999")
        
        resultado = ''
        # Iteramos sobre cada par (valor, símbolo)
        for valor, simbolo in self.valores:
            # Mientras el número sea mayor o igual al valor actual
            while numero >= valor:
                # Añadimos el símbolo correspondiente al resultado
                resultado += simbolo
                # Restamos el valor al número
                numero -= valor
        return resultado

def main():
    # Creamos una instancia del convertidor
    conversor = ConvertidorAñoRomano()
    
    # Mensaje de bienvenida
    print("¡Descubre tu año de nacimiento en números romanos!")
    print("================================================")
    
    # Bucle principal del programa
    while True:
        try:
            # Solicitamos el año al usuario
            año = int(input("\nIngresa tu año de nacimiento (o 0 para salir): "))
            
            # Opción para salir del programa
            if año == 0:
                print("¡Gracias por usar el Convertidor de Años Romanos!")
                break
            
            # Convertimos el año a números romanos
            año_romano = conversor.convertir(año)
            
            # Mostramos el resultado
            print(f"\n¡Wow! Tu año de nacimiento en números romanos es: {año_romano}")
            print(f"Si naciste en el año {año}, en la antigua Roma lo escribirían como {año_romano}")
        
        # Manejo de errores para entradas inválidas
        except ValueError as e:
            print(f"Oops! {str(e)}. Por favor, intenta de nuevo.")

# Punto de entrada del programa
if __name__ == "__main__":
    main()