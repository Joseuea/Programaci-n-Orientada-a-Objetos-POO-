# Programa orientado a objetos para calcular el promedio semanal del clima

class ClimaSemanal:
    def __init__(self):
        self.temperaturas = []

    def ingresar_datos(self):
        print("Ingrese la temperatura para cada día de la semana:")
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        for dia in dias:
            temp = float(input(f"Temperatura del {dia}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        if len(self.temperaturas) == 0:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)

# Función principal
def main():
    clima = ClimaSemanal()
    clima.ingresar_datos()
    promedio = clima.calcular_promedio()
    print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")

# Llamada a la función principal
if __name__ == "__main__":
    main()
