
from dominio import ProblemaFerry
from buscas import busca_ida_estrela


def testar_ida_estrela():

    problema = ProblemaFerry()

    print("========== IDA* COM h2 ==========")

    percurso, expandidos, gerados = busca_ida_estrela(
        problema,
        "h2"
    )

    if percurso is not None:
        print("Solução encontrada!")
        print("Número de travessias:", len(percurso) - 1)
        print("Custo total:", percurso[-1].g)
        print("Nós expandidos:", expandidos)
        print("Nós gerados:", gerados)

        print("\nPercurso encontrado:")

        for i, no in enumerate(percurso):
            print(f"Passo {i}: Estado = {no.estado}")

            if no.accao is not None:
                print("  Acção:", no.accao)
    else:
        print("Não foi encontrada solução.")


if __name__ == "__main__":
    testar_ida_estrela()
