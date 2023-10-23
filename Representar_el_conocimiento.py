# Concepto 1: Simbolismo
# Utilizamos símbolos y relaciones para representar el conocimiento.

# Concepto 2: Ontologías
# Creamos una ontología para definir conceptos y relaciones en el dominio.

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Mamifero(Animal):
    pass

class Ave(Animal):
    pass

# Concepto 3: Redes Semánticas
# Representamos el conocimiento como nodos (conceptos) y arcos (relaciones).

leon = Mamifero("León")
aguila = Ave("Águila")

# Concepto 4: Marcos
# Organizamos el conocimiento en términos de atributos y valores.

leon.color = "Amarillo"
aguila.color = "Marrón"

# Concepto 5: Reglas
# Utilizamos reglas de producción para inferir conocimiento.

def es_predador(animal):
    if isinstance(animal, Mamifero):
        return True
    return False

# Concepto 6: Representación de Grafos
# Modelamos conceptos y relaciones en una estructura de grafo.

# Concepto 7: Aprendizaje Automático y Representaciones Distribuidas (no se implementan aquí)
# Concepto 8: Razonamiento y Toma de Decisiones
# Usamos razonamiento lógico para realizar inferencias.

def clasificar(animal):
    if es_predador(animal):
        return "Es un predador."
    else:
        return "No es un predador."

# Concepto 9: Aplicaciones
# Aplicamos la representación del conocimiento en un contexto específico.

print(f"El {leon.nombre} es de color {leon.color}. {clasificar(leon)}")
print(f"El {aguila.nombre} es de color {aguila.color}. {clasificar(aguila)}")
