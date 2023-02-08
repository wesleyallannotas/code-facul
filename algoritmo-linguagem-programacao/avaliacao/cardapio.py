cardapio = list()

def exibe_menu():
  while True:
    print('''
    -=-=-=-=-= MENU =-=-=-=-=-
    [1] Adicionar pizza no cardápio
    [2] Consultar pizza
    [3] Alterar pizza do cardápio
    [4] Excluir pizza do cardápio
    [5] Exibir cardápio completo
    [6] Exportar cardápio para arquivo texto
    [7] SAIR
    ''')
    opc = int(input('Opção: '))
    if opc == 1:
      print('Cadastro de Pizza:')
      cardapio_cadastrar(*(valida_dados()))
    elif opc == 2:
      iden = int(input('Informe o ID da pizza: '))
      print(f'O index da pizza com o ID {iden} é {cardapio_consulta(iden)}')
      print(cardapio[cardapio_consulta(iden)])
    elif opc == 3:
      iden = int(input('Informe o ID da pizza a ser alterada: '))
      cardapio_alterar(iden, item=valida_dados(objeto=True))
    elif opc == 4:
      iden = int(input('Informe o ID da pizza que sera excluída: '))
      cardapio_remover(iden)
    elif opc == 5:
      cardapio_exibir()
    elif opc == 6:
      cardapio_salvar()
    elif opc == 7:
      break
    else:
      print(f'Opção invalida!')
      exibe_menu()

def valida_dados(objeto=False):
      iden = int(input('ID: '))
      while iden <= 0:
        iden = int(input('Invalido! ID: '))
      nome = str(input('Nome: '))
      ingredientes = list()
      continuar = 'S'
      while continuar == 'S':
        ingredientes.append(str(input('Ingrediente: ')))
        continuar = str(input('Continuar adicionando ingredientes [S/N]: ')).strip().upper()[0]
        while continuar not in 'NS':
            continuar = str(input('ERRO! Informe S ou N, Continuar adicionando ingredientes: ')).strip().upper()[0]
      preco = float(input('Preço: '))
      while preco <= 0.0:
        preco = float(input('Invalido! Preço: '))
      if objeto:
        return {"id":iden, "nome":nome, "ingredientes":ingredientes, "preco":preco}
      return iden, nome, ingredientes, preco

def cardapio_cadastrar(iden, nome, ingredientes, preco):
    global cardapio
    item = dict()
    item["id"] = iden
    item["nome"] = nome
    item["ingredientes"] = ingredientes
    item["preco"] = preco
    cardapio.append(item)

def cardapio_consulta(iden):
  for j, i in enumerate(cardapio):
    if iden == i["id"]:
      return j
  return None
      
def cardapio_alterar(iden, item):
  global cardapio
  alt = cardapio_consulta(iden)
  cardapio[alt]["id"] = item["id"]
  cardapio[alt]["nome"] = item["nome"]
  cardapio[alt]["ingredientes"] = item["ingredientes"]
  cardapio[alt]["preco"] = item["preco"]
  
def cardapio_remover(iden):
  global cardapio
  index = cardapio_consulta(iden)
  cardapio.pop(index)

def cardapio_exibir():
  global cardapio
  # Cabeçalho
  print('-'*100)
  print(f'| {"ID":^5} | {"Nome":^25} | {"Ingredientes":^50} | {"Preço":^7} |')
  print('-'*100)
  # Corpo
  for i in cardapio:
    print(f'| {i["id"]:^5} | {i["nome"]:^25} | {", ".join(i["ingredientes"]):^50} | {i["preco"]:^7.2f} |') 
    print('-'*100)

def cardapio_salvar():
  with open('cardapio.txt', 'w', encoding='utf-8') as arq:
    arq.write('id;nome;ingredientes;preco\n')
    for i in cardapio:
      arq.write(f'{i["id"]};{i["nome"]};{i["ingredientes"]};{i["preco"]:.2f}\n')


# Start
exibe_menu()