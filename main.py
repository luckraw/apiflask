from flask import Flask, jsonify, request

app = Flask(__name__)

post = [
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
def post():
    return jsonify(post)

@app.route('/post', methods=['GET'])
def get_post():
    return jsonify(post)

@app.route('/post/<int:indice>', methods=['GET'])
def get_post_by_indice(indice):
    return jsonify(post[indice])

@app.route('/post', methods=['POST'])
def create_post():
    data = request.get_json()
    data.append(data)
    return jsonify(data, 200)

@app.route('/post/<int:indice>', methods=['PUT'])
def change_post(indice):
    post_alter = request.get_json()
    post[indice].update(post_alter)
    return jsonify(post[indice], 200)

@app.route('/post/<int:indice>', methods=['DELETE'])
def delete_post(indice):
    try:
        if post[indice] is not None:
            del post[indice]
            return jsonify(f'Post deleted successfully. {post[indice]}', 200)
    except:
        return jsonify('Could not find post for deletion', 404)

app.run(port=7777, host='localhost', debug=True)
