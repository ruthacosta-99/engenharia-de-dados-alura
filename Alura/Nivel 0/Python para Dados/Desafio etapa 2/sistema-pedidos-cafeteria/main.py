
cliente_name = input("Nome do cliente: ")
cliente_idade = int(input("Idade do cliente: "))
produto = input("Pedido escolhido: ")
preco = float(input("Preço do produto: "))
quantidade = int(input("Quantidade: "))
clube = input("O cliente é membro do clube de fidelidade? (sim/nao): ")
modo = input("Escolha a opção de entrega:\n1 - Retirar na loja\n2 - Entrega em domicílio\n ")
observacao = input("Deseja deixar alguma observação sobre o pedido? ")

valor = preco * quantidade

if clube == "sim":
    if valor <50:
        desconto = '5%'
        valor_1 = valor - (0.05*valor)
    elif valor >= 50 and valor < 100:
        desconto = '10%'
        valor_1 = valor - (0.10*valor)
    else:
        desconto = '15%'
        valor_1 = valor - (0.15*valor)
else:
    if valor <50:
        desconto = 'sem desconto'
        valor_1 = valor
    elif valor >= 50 and valor < 100:  
        desconto = '5%'
        valor_1 = valor - (0.05*valor)
    else:
        desconto = '10%'
        valor_1 = valor - (0.10*valor)

if modo == "2":
    if valor <50:
        entrega = 'Sim'
        valor_entrega = 8
        valor_2 = 8 + valor_1
    elif valor >= 50 and valor < 100:
        entrega = 'Sim'
        valor_entrega = 5
        valor_2 = 5 + valor_1   
    else:
        entrega = 'Sim'
        valor_entrega = 0
        valor_2 = valor_1
else:
    entrega = 'Não'
    valor_entrega = 0
    valor_2 = valor_1

print("========== CAFETERIA PYTHON ==========")
print(f"Cliente: {cliente_name}")
print(f"Idade: {cliente_idade}")
print(f"Produto: {produto}")
print(f"Quantidade: {quantidade}")
print(f"Preço: R${preco:.2f}")
print("")
print(f"Valor bruto: R${valor:.2f}")
print(f"Desconto: {desconto}")
print(f"Valor com {desconto} de desconto: R$ {valor_1:.2f}")
print("")
print(f"Será entrega: {entrega}")
print(f"Valor da entrega: R${valor_entrega:.2f}")
print(f"Valor final: R${valor_2:.2f}")
print(f"É membro do clube: {clube}")
print("")
if valor_1 >= 80 and clube=="sim":
    print("Cliente ganhou um cookie grátis! 🍪")
else:
    print("Cliente não ganhou brinde! 😢")

print(f"Observação como foi digitada: {observacao}")
print(f"Observação em maiúsculas: {observacao.upper()}")
print(f"Observação em minúsculas: {observacao.lower()}")
print(f"Observação sem espaços no começo e no final: {observacao.strip()}")


