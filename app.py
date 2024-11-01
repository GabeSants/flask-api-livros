from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'título': 'O Senhor dos Anéis - A sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'título': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K. Rowling'
    },
    {
        'id': 3,
        'título': 'Hábitos Atômicos',
        'autor': 'James Clear'
    }
]

@app.route('/')
def home():
    return "Hello World"

# Consultar todos os livros
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar um livro por id
@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
       if livro.get('id') == id:
           return jsonify(livro)
    else:
        return jsonify({"error": "Livro não encontrado"}), 404
       
# Editar um livro por id
@app.route('/livros/<int:id>',methods=['PUT'] )
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
    else:
        return jsonify({"error": "Livro não encontrado"}), 404
    
# Criar um novo livro
@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    novo_id = (max(livro['id'] for livro in livros) + 1) if livros else 1
    novo_livro['id'] = novo_id
    livros.append(novo_livro)
    
    return jsonify(livros), 201

# Excluir um livro por id
@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livros(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            return jsonify({"message": "Livro excluído com sucesso", "livros": livros}), 200
    else:
        return jsonify({"error": "Livro não encontrado", "livros": livros}), 404
    

app.run(port=5000, host='localhost', debug=True )