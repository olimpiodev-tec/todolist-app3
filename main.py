# Importação das bibliotecas
from flask import Flask
from tarefa import buscar_tarefas, buscar_tarefa

# Cria o objeto do flask
app = Flask(__name__)

# Criando nossa primeira rota /api
@app.route('/api')
def index():
    return 'Api rodando'

# Criando a rota que retorna as tarefas
@app.route('/api/tarefas')
def get_tarefas():
    tarefas = buscar_tarefas()
    return tarefas

# Criando a rota para retornar uma única tarefa
@app.route('/api/tarefa/<int:tarefa_id>')
def get_tarefa(tarefa_id):
    tarefa = buscar_tarefa(tarefa_id)
    return tarefa

# Identifica que é o arquivo principal
# E liga o servidor executando o Flask 😊
if __name__ == "__main__":
    app.run(debug=True)

  

