from datetime import datetime
from flask import Flask, request 
from flask_json import FlaskJSON, JsonError, json_response

# Creates Flask instance
app = Flask(__name__)
json = FlaskJSON(app)

# test
@app.route('/')
def test():
    now = datetime.now()
    return json_response(time=now)

todos = [ {'id':1,'task': 'eat dinner'}, {'id': 2, 'task': 'wash car'}, {'id': 3, 'task': 'make flask app'}]

# Get all todos
@app.route("/todos", methods=["GET"])
def getTodos():
    return json_response(todos=todos)

# Get a todo by ID via query string
@app.route("/todo", methods=["GET"]) #:id 
def getTodo():
    id = int(request.args['id'])
    for todo in todos:
        if todo['id'] == id:
           return json_response(todo=todo)

# Adds a todo. Send in body e.g. {"task": "Go to gym"}
@app.route("/todos", methods=["POST"])
def addTodo():
   todo = {'id': len(todos) + 1 ,'task': request.json['task']}
   todos.append(todo)
   return json_response(todo=todo)

# Updates a todo
@app.route("/todos", methods=["PUT"])
def updateTodo():
    id = int(request.json['id'])
    for todo in todos:
        if todo['id'] == id:
            todo= { "id": id, "task": request.json['task'] }
            todos[id - 1] = todo
            return json_response(todo=todo)

    
# Deletes a todo
@app.route("/todos", methods=["DELETE"])
def deleteTodo():
    id = int(request.args['id'])
    for todo in todos:
        if todo['id'] == id:
           del todos[id - 1]
           return '', 204

app.run()