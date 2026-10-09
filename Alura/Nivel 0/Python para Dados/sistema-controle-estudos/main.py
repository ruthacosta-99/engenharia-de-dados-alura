materias = int(input("Digite o número de matérias que você estudou hoje: "))

total_minutos = 0

for i in range(materias):
    print(f"===== ESTUDO {i + 1} =====")
    nome_materia = input("Digite o nome da matéria: ")
    tempo_estudo = float(input(f"Digite o tempo de estudo em minutos para {nome_materia}: "))
    print(" ")

    total_minutos += tempo_estudo

total_horas = total_minutos / 60

revisao = input("Deseja revisar algum tópico? (s/n): ").strip().lower()
topicos_revisao = 0

while revisao == 's':
    topicos_revisao += 1
    nome_materia_revisao = input("Digite o tópico que precisa revisar: ")
    revisao = input("Deseja adicionar outro tópico? (s/n): ").strip().lower()

print(" ")
print(" ========== RESUMO DO DIA ==========")
print(f"Matérias estudadas: {materias}")
print(f"Tempo total de estudo: {total_horas:.2f} horas")
print(f"Tópicos adicionados para revisão: {topicos_revisao}")

if total_horas > 2:
    print("🔥 Você estudou mais de 2 horas hoje!")
else:
    print("📚 Continue se esforçando! Cada minuto de estudo conta.")