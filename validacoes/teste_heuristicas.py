
from dominio import ProblemaFerry


problema = ProblemaFerry()

estado = problema.estado_inicial()

valor_h0 = problema.heuristica(estado, "h0")
valor_h1 = problema.heuristica(estado, "h1")
valor_h2 = problema.heuristica(estado, "h2")

print("Estado inicial:", estado)

print("\nValores das heurísticas:")
print("h0 =", valor_h0)
print("h1 =", valor_h1)
print("h2 =", valor_h2)

print("\nVerificação de dominância:")

if valor_h2 >= valor_h1:
    print("h2 é maior ou igual a h1 neste estado.")
else:
    print("h2 é inferior a h1 neste estado.")
