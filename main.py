from services.avaliador import Avaliador
from services.repositorio import Repositorio


def menu():
    print("==============================")
    print("(T) Interesse em tecnologia")
    print("(A) Aptidão analítica")
    print("(C) Criatividade")
    print("(P) Afinidade com pessoas")
    print("==============================\n")
    print(" (1) - Avaliar perfil")
    print(" (2) - Listar perfis")
    print(" (0) - SAIR\n")


def coletar_dados():
    print("\nResponda com 0 (não) ou 1 (sim):\n")

    T = int(input("1 - Interesse em tecnologia? "))
    A = int(input("2 - Alta aptidão analítica? "))
    C = int(input("3 - É muito criativo? "))
    P = int(input("4 - Tem afinidade com pessoas? "))

    return [T, A, C, P]


def main():
    avaliador = Avaliador()
    repo = Repositorio()

    while True:
        menu()
        op = input("QUAL SERIA SUA OPÇÃO?\n")

        if op == "1":
            print("\nVamos avaliar seu perfil...\n")
            nome = input("Digite seu nome: ")
            respostas = coletar_dados()

            (
                prof1, afi1,
                prof2, afi2
            ) = avaliador.analisar(respostas)

            print("\n===== RESULTADO =====")
            print(f"1ª opção recomendada: {prof1} ({afi1}%)")
            print(f"2ª opção recomendada: {prof2} ({afi2}%)")

            # salva apenas a melhor profissão
            repo.salvar_perfil(nome, respostas, prof1, afi1,prof2,afi2)


        elif op == "2":
            print("\n===== LISTA DE PERFIS =====\n")
            perfis = repo.listar_todos()

            if not perfis:
                print("Nenhum perfil cadastrado ainda.\n")
            else:
                for p in perfis:
                    prof1 = p.get("melhor_profissao", "Não informado")
                    afi1 = p.get("afinidade_1", "N/A")

                    prof2 = p.get("segunda_profissao", "Nenhuma (perfil antigo)")
                    afi2 = p.get("afinidade_2", "N/A")

                    print(f"- {p['nome']} → {prof1} ({afi1}%)")
                    print(f"   2ª opção: {prof2} ({afi2}%)\n")

                print()

        elif op == "0":
            print("\nSaindo... até breve!\n")
            break

        else:
            print("OPÇÃO NÃO CORRESPONDENTE\n")


if __name__ == "__main__":
    main()
