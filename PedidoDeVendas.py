import random 
import time

loja = {}
estoquetotal = 1
total = 0
valor = 0
pagamento = ["pix","dinheiro","debito","credito"]
pix = 0
dinheiro = 0
debito = 0
credito = 0

while True:

 print("\n ---Pedidos de venda---\n")
 print("1 - Adicionar no estoque")
 print("2 - conferir estoque")
 print("3 - atender cliente")
 print("4 - Fechar caixa")
 print("5 - Finalizar sistema")

 opcao = int(input("Selecione uma opcão: "))

 if opcao == 1:
    nome = input("\nDigite o nome do produto: ")
    quantidade = int(input("\nDigite a quantidade no estoque: "))
    estoquetotal = estoquetotal + quantidade
    preco = input("\nDigite o preço do produto: R$")
    preco = float(preco.replace(",", "."))
    loja[nome] = {
      "quantidade": quantidade,
      "preco": preco
    }
    print("Produto adicionado ")

 elif opcao == 2:
   print("\n Estoque")
   if len(loja) == 0:
      print("Estoque vazio...")

   else:
    for nome, dados in loja.items():
      quantidade = dados["quantidade"]
      preco = dados ["preco"]
      print("Nome: {} Quantidade: {} Preço: R${:.2f}\n".format (nome, quantidade , preco, ))
   print("Total de {} produtos".format(estoquetotal-1))

 elif opcao == 3:
     
   if estoquetotal == 1:
           print("\nNão e possivel vender com o\nEstoque zerado..")
     
   else:  
    itens = random.randint (1 , 10 )
    for i in range (itens):
       
        if len(loja) >=1:
     
         nome = random.choice(list(loja.keys()))
       
         if loja [nome]["quantidade"] == 0:
          del loja[nome]
          
          
         else:
          nome in loja
          loja[nome]["quantidade"] -= 1 
          valor = valor + loja[nome]["preco"]
          total = total + 1
          estoquetotal -= 1
      
          print("\n1 uni de {}  R${:.2f} ".format(nome, loja[nome]["preco"]))
          time.sleep(0.6)
             
    print("\nTotal de produtos: {}\nValor total R${:.2f}".format(total,valor))

    pagamento1 = random.choice(pagamento)

    if pagamento1 == "pix":
     pix = pix + valor
     print("pagamento em {} efetuado".format(pagamento1))

    elif pagamento1 == "dinheiro":
     print("pagamento em {} efetuado".format(pagamento1))
     dinheiro = dinheiro + valor

    elif pagamento1 == "credito":
     print("pagamento em {} efetuado".format(pagamento1))
     credito = credito+valor

    else:
     print("pagamento em {} efetuado".format(pagamento1))
     debito = debito + valor
      
   

 elif opcao == 4:
   total=debito+credito+dinheiro+pix
   print("    pix   | R${:.2f}\n  credito | R${:.2f}\n   debito | R${:.2f}\n dinheiro | R${:.2f}\nO valor total de vendas foi R${:.2f}".format(pix, credito , debito, dinheiro, total))
   print ("\nFinalizando sistema...")
   pix = 0
   dinheiro = 0 
   debito = 0
   credito = 0
   break

 elif opcao == 5:
  print("Finalizando sistema...")
  break

 else:
   print("\nNão entendi...")
   
 total = 0
 valor = 0  