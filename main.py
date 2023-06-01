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
def get_post_by_indice(index):
    return jsonify(post[index])

@app.route('/post', methods=['POST'])
def create_post():
    data = request.get_json()
    data.append(data)
    return jsonify(data, 200)

@app.route('/post/<int:indice>', methods=['PUT'])
def update_post(index):
    post_alter = request.get_json()
    post[index].update(post_alter)
    return jsonify(post[index], 200)

@app.route('/post/<int:indice>', methods=['DELETE'])
def delete_post(index):
    try:
        if post[index] is not None:
            del post[index]
            return jsonify(f'Post deleted successfully. {post[index]}', 200)
    except:
        return jsonify('Could not find post for deletion', 404)

app.run(port=7777, host='localhost', debug=True)
