import math

def log_base(a, b):
    return math.log(a) / math.log(b)

def calcular_juros_compostos():
    print("=== Calculadora de Juros Compostos ===")
    print("Informe os valores que você TEM. Digite 'n' para a variável que deseja descobrir.")
    
    pv_input = input("Valor Presente (PV): ").replace(",", ".")
    fv_input = input("Valor Futuro (FV): ").replace(",", ".")
    i_input = input("Taxa de Juros (% ao período): ").replace(",", ".")
    n_input = input("Tempo (nº de períodos): ").replace(",", ".")

    # Processar entradas
    PV = float(pv_input) if pv_input.lower() != 'n' else None
    FV = float(fv_input) if fv_input.lower() != 'n' else None
    i = float(i_input)/100 if i_input.lower() != 'n' else None
    n = float(n_input) if n_input.lower() != 'n' else None

    try:
        if PV is None and FV is not None and i is not None and n is not None:
            PV = FV / ((1 + i) ** n)
            print(f"\n=> Valor Presente (PV) = R$ {PV:.2f}")

        elif FV is None and PV is not None and i is not None and n is not None:
            FV = PV * ((1 + i) ** n)
            print(f"\n=> Valor Futuro (FV) = R$ {FV:.2f}")

        elif i is None and PV is not None and FV is not None and n is not None:
            i = (FV / PV) ** (1 / n) - 1
            print(f"\n=> Taxa de Juros (i) = {i * 100:.4f}% ao período")

        elif n is None and PV is not None and FV is not None and i is not None:
            n = log_base(FV / PV, 1 + i)
            print(f"\n=> Tempo (n) = {n:.3f} períodos")

        else:
            print("\n Erro: Você deve deixar exatamente UMA variável como 'n' (desconhecida).")
    except:
        print("\n Houve um erro ao tentar calcular. Verifique os valores inseridos.")

# Executar
calcular_juros_compostos()
