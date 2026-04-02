from crud import criar_registro, listar_todos, listar_por_grupo, atualizar_registro, deletar_registro

def menu():
    print("\n--- CRUD JSON ---")
    print("1. Criar registro")
    print("2. Listar todos os registros")
    print("3. Listar registros por grupo")
    print("4. Atualizar registro")
    print("5. Deletar registro")
    print("0. Sair")
    return input("Escolha uma opção: ")

def main():
    while True:
        opcao = menu()
        if opcao == "1":
            grupo = input("Grupo (alunos/professores): ")
            id_registro = input("ID: ")
            nome = input("Nome: ")
            criar_registro(grupo, {"id": id_registro, "nome": nome})
        elif opcao == "2":
            print(listar_todos())
        elif opcao == "3":
            grupo = input("Grupo (alunos/professores): ")
            print(listar_por_grupo(grupo))
        elif opcao == "4":
            grupo = input("Grupo (alunos/professores): ")
            id_registro = input("ID do registro a atualizar: ")
            nome = input("Novo nome: ")
            atualizar_registro(grupo, id_registro, {"nome": nome})
        elif opcao == "5":
            grupo = input("Grupo (alunos/professores): ")
            id_registro = input("ID do registro a deletar: ")
            deletar_registro(grupo, id_registro)
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()