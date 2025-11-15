# Importa a conexão criada
from conexao import get_conexao

# Importa a biblioteca psycog2
from psycopg2.extras import RealDictCursor

# Importa o jsonfy do flask para 
# retornar os dados no formato json
from flask import jsonify

def buscar_tarefas():
    conn = get_conexao()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(
        "SELECT id, nome, descricao FROM tarefas;"
    )
    # Busca todos os registros na tabela
    tarefas = cursor.fetchall()

    # Fecha as conexões
    cursor.close()
    conn.close()

    return jsonify(tarefas)

def buscar_tarefa(tarefa_id):
    conn = get_conexao()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(
        "SELECT id, nome, descricao FROM tarefas WHERE id=%s",
        (tarefa_id,)
    )
    tarefa = cursor.fetchone()
    cursor.close()
    conn.close()

    return jsonify(tarefa)

def apagar_tarefa(tarefa_id):
    conn = get_conexao()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM tarefas WHERE id=%s",
        (tarefa_id,)
    )
    conn.commit()
    cursor.close()
    conn.close()

def criar_tarefa(nome, descricao):
    conn = get_conexao()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tarefas (nome, descricao) VALUES(%s, %s)",
        (nome, descricao)
    )
    conn.commit()
    cursor.close()
    conn.close()

def atualizar_tarefa(nome, descricao, tarefa_id):
    conn = get_conexao()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tarefas SET nome=%s, descricao=%s WHERE id=%s",
        (nome, descricao, tarefa_id)
    )
    conn.commit()
    cursor.close()
    conn.close()