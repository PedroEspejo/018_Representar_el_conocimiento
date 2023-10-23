# Representación de conocimiento en marcos
class AnimalFrame:
    def __init__(self, nombre, tipo, color):
        self.nombre = nombre
        self.tipo = tipo
        self.color = color

leon = AnimalFrame("León", "mamífero", "amarillo")
aguila = AnimalFrame("Águila", "ave", "marrón")

print(f"{leon.nombre} es un {leon.tipo} de color {leon.color}.")
print(f"{aguila.nombre} es un {aguila.tipo} de color {aguila.color}.")
