from datetime import datetime

especialidades = [
    "Imunologia",
    "Angiologia",
    "Cardiologia",
    "ClinicaMedica",
    "Dermatologia",
    "Endocrinologia",
    "Fonoaudiologia",
    "Gastroenterologia",
    "Geriatria",
    "Ginecologia",
    "Hematologia",
    "MedicinaPreventiva",
    "Nefrologia",
    "Neurologia",
    "Nutricao",
    "Obstetricia",
    "Odontologia",
    "Oftalmologia",
    "Oncologia",
    "Ortopedia",
    "Otorrinolaringologia",
    "Pediatria",
    "Psicologia",
    "Proctologia",
    "Psiquiatria",
    "Reumatologia",
    "Urologia"
]

def mostrar_menu():
    print("\n===== Sistema de Agendamento =====")
    print("1. Agendar Consulta")
    print("2. Visualizar Consultas Agendadas")
    print("3. Sair")

def agendar_consulta(consultas):
    nome = input("Digite seu nome: ")

    # Lista
    print("\nEspecialidades Disponíveis:")
    for i, especialidade in enumerate(especialidades, start=1):
        print(f"{i}. {especialidade}")

    # Validar a escolha da especialidade
    while True:
        escolha_especialidade = input("Escolha o número correspondente à especialidade desejada: ")
        try:
            escolha_especialidade = int(escolha_especialidade)
            if 1 <= escolha_especialidade <= len(especialidades):
                especialidade = especialidades[escolha_especialidade - 1]
                break
            else:
                print("Número fora do intervalo. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

    # Validar a data
    while True:
        data_str = input("Digite a data da consulta (dd/mm/aaaa): ")
        try:
            data = datetime.strptime(data_str, "%d/%m/%Y")
            break
        except ValueError:
            print("Data inválida. Tente novamente no formato dd/mm/aaaa.")

    # Validar o horário
    while True:
        horario_str = input("Digite o horário da consulta (HH:MM): ")
        try:
            horario = datetime.strptime(horario_str, "%H:%M")
            break
        except ValueError:
            print("Horário inválido. Tente novamente no formato HH:MM.")

    consulta = {
        "Nome": nome,
        "Especialidade": especialidade,
        "Data": data.strftime("%d/%m/%Y"),
        "Horario": horario.strftime("%H:%M")
    }

    consultas.append(consulta)
    print("Consulta agendada com sucesso!")

def visualizar_consultas(consultas):
    print("\n--- Consultas Agendadas ---")
    for consulta in consultas:
        print(f"Nome: {consulta['Nome']}, Especialidade: {consulta['Especialidade']}, Data: {consulta['Data']}, Horário: {consulta['Horario']}")
    print("------------------------------")

def main():
    consultas = []

    while True:
        mostrar_menu()
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            agendar_consulta(consultas)
        elif opcao == "2":
            visualizar_consultas(consultas)
        elif opcao == "3":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
