# Clase para convertir números romanos a años

class DescifradorRomano:
    def __init__(self):
        # Diccionario que mapea símbolos romanos a valores enteros
        self.simbolos = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

    def convertir(self, numero_romano):
        # Validación inicial: comprueba si todos los caracteres son válidos
        if not all(char in self.simbolos for char in numero_romano):
            raise ValueError("El número romano contiene caracteres no válidos")

        total = 0
        prev_valor = 0

        # Iteramos sobre el número romano de derecha a izquierda
        for simbolo in reversed(numero_romano):
            valor = self.simbolos[simbolo]
            
            # Si el valor actual es mayor o igual al anterior, lo sumamos
            if valor >= prev_valor:
                total += valor
            # Si es menor, lo restamos (casos como IV, IX, XL, etc.)
            else:
                total -= valor
            
            prev_valor = valor

        return total

def main():
    descifrador = DescifradorRomano()
    print("¡Bienvenido al Descifrador de Números Romanos!")
    print("=============================================")

    while True:
        numero_romano = input("\nIngresa un número romano (o 'salir' para terminar): ").upper()
        
        if numero_romano == 'SALIR':
            print("¡Gracias por usar el Descifrador de Números Romanos!")
            break

        try:
            resultado = descifrador.convertir(numero_romano)
            print(f"\n¡Eureka! El número romano {numero_romano} equivale a {resultado} en nuestro sistema numérico.")
            print(f"¿Sabías que los antiguos romanos usaban {numero_romano} para representar el número {resultado}?")
        except ValueError as e:
            print(f"Oops! {str(e)}. Por favor, intenta de nuevo con un número romano válido.")

if __name__ == "__main__":
    main()