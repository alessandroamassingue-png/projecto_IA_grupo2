
from dominio import ProblemaFerry

# 1. Criar o problema original.
problema_original = ProblemaFerry()

print("Problema original:")
print("Estado inicial:", problema_original.estado_inicial())
print("Estado objectivo:", (511, 1))

# 2. Criar um problema personalizado.
problema_personalizado = ProblemaFerry(
    estado_inicial=(12, 0)
)

print("\nProblema personalizado:")
print("Estado inicial:", problema_personalizado.estado_inicial())

# 3. Verificar se o objectivo continua correcto.
print(
    "\nObjectivo reconhecido:",
    problema_personalizado.e_objectivo((511, 1))
)

# 4. Verificar se o estado inicial é seguro.
print(
    "Estado inicial seguro:",
    problema_personalizado.estado_seguro(
        problema_personalizado.estado_inicial()[0]
    )
)

# 5. Verificar se o estado inicial tem acções.
print(
    "Número de acções disponíveis:",
    len(problema_personalizado.accoes(
        problema_personalizado.estado_inicial()
    ))
)
