import json
import os

# Caminho do arquivo JSON
DATA_FILE = "data.json"

# Função para ler o JSON
def ler_dados():
    """Lê o arquivo JSON e retorna os dados como dicionário."""
    if not os.path.exists(DATA_FILE):
        return {"alunos": [], "professores": []}
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

# Função para salvar dados no JSON
def salvar_dados(dados):
    """Salva o dicionário de dados no arquivo JSON."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(dados, file, indent=4, ensure_ascii=False)

# -------------------- CREATE --------------------
def criar_registro(grupo, registro):
    """
    Adiciona um novo registro a um grupo.
    registro deve ser um dicionário com pelo menos 'id' e 'nome'.
    """
    dados = ler_dados()
    if grupo not in dados:
        dados[grupo] = []
    dados[grupo].append(registro)
    salvar_dados(dados)
    print(f"Registro adicionado ao grupo '{grupo}'.")

# -------------------- READ --------------------
def listar_todos():
    """Lista todos os registros do JSON."""
    dados = ler_dados()
    return dados

def listar_por_grupo(grupo):
    """Lista registros de um grupo específico."""
    dados = ler_dados()
    return dados.get(grupo, [])

# -------------------- UPDATE --------------------
def atualizar_registro(grupo, id_registro, novos_dados):
    """Atualiza um registro específico usando o id."""
    dados = ler_dados()
    registros = dados.get(grupo, [])
    for i, registro in enumerate(registros):
        if registro.get("id") == id_registro:
            registros[i].update(novos_dados)
            salvar_dados(dados)
            print(f"Registro com id {id_registro} atualizado no grupo '{grupo}'.")
            return
    print(f"Registro com id {id_registro} não encontrado no grupo '{grupo}'.")

# -------------------- DELETE --------------------
def deletar_registro(grupo, id_registro):
    """Deleta um registro específico usando o id."""
    dados = ler_dados()
    registros = dados.get(grupo, [])
    for i, registro in enumerate(registros):
        if registro.get("id") == id_registro:
            del registros[i]
            salvar_dados(dados)
            print(f"Registro com id {id_registro} deletado do grupo '{grupo}'.")
            return
    print(f"Registro com id {id_registro} não encontrado no grupo '{grupo}'.")