dados estão no formato: "nome_completo;cargo_ou_setor;telefone_ou_cpf"
dados_brutos = [
   "  carlos eduardo silva;desenvolvedor;11988887777  ",
   "  ana paula mendes;analista de rh;21977776666  ",
   "  roberto carlos oliveira;gerente de projetos;31966665555  "


def limpar_e_formatar_texto(texto):
   """
   FUNÇÃO 1:
   - Deve receber uma string.
   - Deve remover espaços extras das pontas (.strip()).
   - Deve converter o texto para letras MAIÚSCULAS (.upper()).
   - Retorna o texto devidamente formatado.
   """
   # TODO: Implemente a lógica da Função 1 aqui
   pass


def extrair_codigo_ou_ddd(dado):
   """
   FUNÇÃO 2:
   - Deve receber um dado em formato de string (ex: telefone ou CPF).
   - Deve remover espaços das pontas.
   - Deve utilizar FATIAMENTO DE STRING [x:y] para extrair os 2 primeiros dígitos (ex: DDD).
   - Retorna apenas os dígitos extraídos.
   """
   # TODO: Implemente a lógica da Função 2 aqui
   pass


def processar_e_exibir_cadastros(lista_dados):
   """
   FUNÇÃO 3:
   - Deve receber a lista de cadastros brutos como parâmetro.
   - Deve utilizar um laço FOR para percorrer cada item da lista.
   - Em cada iteração do for:
       1. Separar as partes usando .split(";")
       2. Chamar a Função 1 para formatar o Nome e o Cargo.
       3. Chamar a Função 2 para extrair o DDD/Código do telefone.
       4. Exibir o resultado final formatado na tela com f-string.
   - Retorna a quantidade total de registros processados.
   """
   # TODO: Implemente a lógica da Função 3 aqui
   pass
]

def main():
   print("==================================================")
   print("     SISTEMA DE GESTÃO MODULARIZADO - AV2        ")
   print("==================================================\n")

   print("Iniciando o processamento dos dados...\n")

   # TODO: Faça a chamada da Função 3 passando a lista 'dados_brutos'
   # e armazene o retorno em uma variável 'total_processado'.
   
   # TODO: Exiba uma mensagem final mostrando a quantidade total de registros processados.

   print("\n==================================================")
   print("             PROCESSAMENTO CONCLUÍDO              ")
   print("==================================================")


# Execução do programa
if __name__ == "__main__":
   main()

