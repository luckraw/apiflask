from flask import Flask, jsonify, request

app = Flask(__name__)

postagens = [
    {'title': 'evangelho de sangue',
     'autor': 'clive barker'
     },
    {
        'title': 'call of cthulhu',
        'autor': 'HP Lovecraft'
    },
    {
        'title': 'the shining',
        'autor': 'stephen king'
    }
]

@app.route('/')
def obter_postagens():
    return jsonify(postagens)

@app.rout('/postagens', methods=['GET'])
def obter_postagens():
    return jsonify(postagens)

@app.route('/postagens/<int:indice>', methods=['GET'])
def obter_postagens_porindice(indice):
    return jsonify(postagens[indice])

@app.route('/postagem', methods=['POST'])
def fazer_postagem():
    dados = request.get_json()
    dados.append(dados)
    return jsonify(dados, 200)

@app.route('/postegem/<int:indice>', methods=['PUT'])
def alterar_postagem(indice):
    postagem_alterada = request.get_json()
    postagens[indice].update(postagem_alterada)
    return jsonify(postagens[indice], 200)

@app.doute('/postagem/<int:indice>', methods=['DELETE'])
def excluir_postagem(indice):
    try:
        if postagens[indice] is not None:
            del postagens[indice]
            return jsonify(f'Postagem excluída com sucesso. {postagens[indice]}', 200)
    except:
        return jsonify('Não foi possível encontrar a postagem para exclusão', 404)

app.run(port=7777, host='localhost', debug=True)
