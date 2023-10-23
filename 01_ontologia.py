# Usando la biblioteca rdflib para trabajar con ontologías RDF
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS

g = Graph()
ex = Namespace("http://example.org/")

# Definir conceptos y relaciones en una ontología
g.add((ex.Dog, RDF.type, RDFS.Class))
g.add((ex.hasLegs, RDF.type, RDF.Property))

# Realizar consultas en la ontología
for s, p, o in g.triples((None, RDF.type, RDFS.Class)):
    print(f"Clase: {s}")
for s, p, o in g.triples((None, RDF.type, RDF.Property)):
    print(f"Propiedad: {s}")
