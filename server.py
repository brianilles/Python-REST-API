from datetime import datetime
from flask import Flask, request 
from flask_json import FlaskJSON, JsonError, json_response

# Creates Flask instance
app = Flask(__name__)
json = FlaskJSON(app)

@app.route('/')
def test():
    now = datetime.now()
    return json_response(time=now)

todos = [ {'id':1,'task': 'eat dinner'}, {'id': 2, 'task': 'wash car'}, {'id': 3, 'task': 'make flask app'}]

@app.route("/todos", methods=["GET"])
def getTodos():
    return json_response(todos=todos)

@app.route("/todo", methods=["GET"]) #:id 
def getTodo():
    id = int(request.args['id'])
    print(id)
    for todo in todos:
        if todo['id'] == id:
           return json_response(todo=todo)

app.run()