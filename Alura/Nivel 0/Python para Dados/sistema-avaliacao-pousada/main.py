name = input("Nome do Hospede? ")
age = int(input("Idade do Hospede? "))
height = float(input("Altura em metros do Hospede? "))

valor_diaria = 205.33
pessoas = int(input("Quantas pessoas vão se hospedar? "))
dias = int(input("Quantos dias de estadia? "))
valor_total = valor_diaria * pessoas * dias

limpeza = float(input("Qual sua nota para a limpeza? "))
conforto = float(input("Qual sua nota para o conforto? "))
atendimento = float(input("Qual sua nota para o atendimento? "))
media = (limpeza + conforto + atendimento) / 3
ponderada = (limpeza * 0.2) + (conforto * 0.3) + (atendimento * 0.5)

comentario = input("Deixe seu comentário sobre a estadia: ")

print('---------- RESUMO DA ESTADIA ----------')

print(f"Hospede: {name}!\nIdade: {age} anos\nAltura: {height} metros.\n")

print(f"Valor total da estadia: R$ {valor_total:.2f}\nPessoas: {pessoas}\nDias de estadia: {dias}\n")

print(f"Valor por pessoa: R$ {valor_total / pessoas:.2f}\nValor medio por diaria: R$ {valor_diaria:.2f}\nValor inteiro por pessoa: {valor_total // pessoas}\nValor restante: R$ {valor_total % pessoas:.2f}\n")

print('---------- AVALIAÇÃO ----------')
print(f"Limpeza: {limpeza}\nConforto: {conforto}\nAtendimento: {atendimento}\nMedia: {media:.2f}\nPonderada: {ponderada:.2f}\n")

print('---------- COMENTARIO ----------')
print(f"Comentário: {comentario}\nMaiúsculas: {comentario.upper()}\nMinúsculas: {comentario.lower()}\nCensurado: {comentario.replace('a', '@')}\n")