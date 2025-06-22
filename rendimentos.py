from datetime import datetime

investimentos = ["CDB", "LCI", "LCA"]

impostos_longo_prazo = [
    (180, 22.5),
    (360, 20.0),
    (720, 17.5),
    (721, 17.5)
]

impostos_curto_prazo = [
    (180, 22.5),
    (181, 20.9)
]

impostos_acoes = 15.0

hoje = datetime.now()

vencimento = datetime.now()

valor = input("Valor: ")

menu_texto = "Tipo de Investimento:\n"

for i, nome_investimento in enumerate(investimentos):
    menu_texto += f"({i + 1}) {nome_investimento}\n"

while True:
    try:
        tipo_str = input(menu_texto)
        tipo_num = int(tipo_str)

        if 1 <= tipo_num <= len(investimentos):
            investimento_selecionado = investimentos[tipo_num -1]
            print(f"\nVocê selecionou: {investimento_selecionado}")
            break
        else:
            print(f"Por favor, digite um número entre 1 e {len(investimentos)}.\n")
    except ValueError:
        print("Por favor, digite apenas o número correspondente à opção.\n")

while (True):
    cdi = float(input("CDI: "))
    if cdi > 0 and cdi < 1000:
        break
    else:
        print("Digite o valor correto da porcentagem do CDI.")

while (True):
    vencimento_input = input("Vencimento: ")
    try:
        vencimento = datetime.strptime(vencimento_input, "%d/%m/%Y").date()
        break
    except:
        print("Formato de data inválido, use DD/MM/AAAA.")