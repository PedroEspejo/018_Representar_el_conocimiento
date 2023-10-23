# Representación de relaciones en una red semántica
semantic_network = {
    "perro": ["mamífero", "animal"],
    "gato": ["mamífero", "animal"],
    "mamífero": ["animal"],
    "animal": []
}

# Consulta de relaciones para un concepto
concepto = "perro"
relaciones = semantic_network.get(concepto, [])
print(f"Relaciones de {concepto}: {relaciones}")
