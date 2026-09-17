
dados_brutos = [
    "  carlos eduardo silva;desenvolvedor;11988887777  ",
    "  ana paula mendes;analista de rh;21977776666  ",
    "  roberto carlos oliveira;gerente de projetos;31966665555  "
]

def limpar_e_formatar_texto(texto):
    """
    FUNÇÃO 1:
    Remove espaços das pontas e transforma o texto em letras maiúsculas.
    """
    texto = texto.strip()
    texto = texto.upper()

    return texto


def extrair_codigo_ou_ddd(dado):
    """
    FUNÇÃO 2:
    Remove espaços das pontas e pega os dois primeiros dígitos
    usando fatiamento de string.
    """
    dado = dado.strip()
    codigo = dado[0:2]

    return codigo


def processar_e_exibir_cadastros(lista_dados):
    """
    FUNÇÃO 3:
    Percorre a lista, separa os dados, formata nome e cargo,
    pega o DDD e exibe os resultados.
    """

    total = 0

    for cadastro in lista_dados:

        partes = cadastro.split(";")

        nome = partes[0]
        cargo = partes[1]
        telefone = partes[2]

        nome = limpar_e_formatar_texto(nome)
        cargo = limpar_e_formatar_texto(cargo)

        ddd = extrair_codigo_ou_ddd(telefone)

        print(f"Nome: {nome}")
        print(f"Cargo/Setor: {cargo}")
        print(f"DDD: {ddd}")
        print("------------------------------------------")

        total += 1

    return total

def main():

    print("==================================================")
    print("     SISTEMA DE GESTÃO MODULARIZADO - AV2")
    print("==================================================\n")

    print("Iniciando o processamento dos dados...\n")

    total_processado = processar_e_exibir_cadastros(dados_brutos)

    print(f"Total de registros processados: {total_processado}")

    print("\n==================================================")
    print("             PROCESSAMENTO CONCLUÍDO")
    print("==================================================")

if __name__ == "__main__":
    main()
