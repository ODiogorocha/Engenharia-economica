def questao1():
    print("\n=== Questão 1 - Taxa Efetiva Anual ===")

    matricula = input("Digite o número da sua matrícula: ")

    try:
        ultimo_digito = int(matricula[-1])
        taxa_semestral_percentual = ultimo_digito
    except:
        print("Erro: matrícula inválida. Digite apenas números.")
        return

    print(f"\nÚltimo dígito da matrícula: {ultimo_digito}")
    print(f"Taxa nominal ao semestre (X): {taxa_semestral_percentual}%")

    print("\n>: Fórmulas usadas:")
    print("1. Taxa mensal: i_m = i_s / 6")
    print("2. Taxa efetiva anual: i_eff = (1 + i_m)^12 - 1")

    taxa_semestral = taxa_semestral_percentual / 100
    taxa_mensal = taxa_semestral / 6
    taxa_efetiva_anual = (1 + taxa_mensal) ** 12 - 1

    print(f"\nTaxa mensal equivalente: {taxa_mensal*100:.4f}%")
    print(f"Taxa efetiva anual equivalente: {taxa_efetiva_anual*100:.2f}% a.a.")


def questao2():
    print("\n=== Questão 2 - Cálculo da Inflação Esperada ===")

    print("\n>: Fórmula usada:")
    print("1. Relação entre taxas: (1 + i_nom) = (1 + i_real) × (1 + i_inf)")
    print("2. Isolando a inflação: i_inf = (1 + i_nom) / (1 + i_real) - 1")

    juros_global_percentual = 15
    juros_real_percentual = 0.5

    i_nom = juros_global_percentual / 100
    i_real = juros_real_percentual / 100
    i_inf = (1 + i_nom) / (1 + i_real) - 1

    print(f"\nJuros nominal (global): {i_nom*100:.2f}% a.m.")
    print(f"Juros real: {i_real*100:.2f}% a.m.")
    print(f"Inflação esperada: {i_inf*100:.2f}% a.m.")


def questao3():
    print("\n=== Questão 3 - Melhor Investimento em 3 anos ===")

    print("\n>: Fórmulas usadas para cada investimento:")
    print("1. Juros compostos: FV = PV × (1 + i)^n")
    print("2. Conversões:")
    print("   - Taxa anual → mensal: i_m = (1 + i_a)^(1/12) - 1")
    print("   - Inflação mensal: i = (1 + i_a)^(1/12) - 1\n")

    capital_inicial = 12500.00
    prazo_total_meses = 36
    prazo_total_anos = 3
    inflacao_anual = 0.04
    inflacao_mensal = (1 + inflacao_anual) ** (1/12) - 1
    resultados = []

    # Opção A
    taxa_aa_a = 0.11
    taxa_mensal_a = (1 + taxa_aa_a) ** (1/12) - 1
    montante_a = capital_inicial * (1 + taxa_mensal_a) ** prazo_total_meses
    resultados.append(("A", montante_a))

    # Opção B
    if capital_inicial < 13500:
        montante_b = 0
    else:
        taxa_trimestre_b = 0.035
        n_trimestres = prazo_total_meses // 3
        montante_b = capital_inicial * (1 + taxa_trimestre_b) ** n_trimestres
    resultados.append(("B", montante_b))

    # Opção C
    taxa_aa_c = 0.125
    montante_c = capital_inicial * (1 + taxa_aa_c) ** prazo_total_anos
    resultados.append(("C", montante_c))

    # Opção D
    taxa_mensal_d = 0.006 + inflacao_mensal
    montante_d = capital_inicial * (1 + taxa_mensal_d) ** prazo_total_meses
    resultados.append(("D", montante_d))

    melhor_opcao = max(resultados, key=lambda x: x[1])

    print(f"\nCapital disponível: R$ {capital_inicial:,.2f}")
    for opcao, valor in resultados:
        if valor == 0:
            print(f"Opção {opcao}: investimento não disponível")
        else:
            print(f"Opção {opcao}: R$ {valor:,.2f}")
    print(f"\n=> Melhor opção: Opção {melhor_opcao[0]} com R$ {melhor_opcao[1]:,.2f}")


def menu():
    while True:
        print("\n=== Menu ===")
        print("1 - Questão 1: Taxa efetiva anual equivalente")
        print("2 - Questão 2: Inflação esperada")
        print("3 - Questão 3: Melhor investimento em 3 anos")
        print("0 - Sair")
        escolha = input("Escolha a questão (0 a 3): ")

        if escolha == "1":
            questao1()
        elif escolha == "2":
            questao2()
        elif escolha == "3":
            questao3()
        elif escolha == "0":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Executa o menu
menu()
