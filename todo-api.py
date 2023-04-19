from flask import Flask, request, jsonify, render_template

todos = [
    {
        "done": True,
        "label": "Sample Todo 1"
    },
    {
        "done": True,
        "label": "Sample Todo 2"
    }
]

app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def todos_get():
    return jsonify (todos)

@app.route('/todos', methods=['POST'])
def todos_post():
    tarea = request.get_json()
    todos.append(tarea)
    return jsonify (todos)

@app.route('/todos/<int:id>', methods=['DELETE'])
def todos_del(id):
    del todos[id]
    return jsonify (todos)

@app.route('/', methods=['GET'])
def html():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port="5000")