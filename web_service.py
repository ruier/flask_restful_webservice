#!/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/appname/module/rest/task', methods=['GET'])
def get_tasks():
    return jsonify({"modid":"123","name":"abc","status":"ok","remark":"good"})

@app.route('/appname/module/rest/user', methods=['GET'])
def get_user():
    return jsonify({'user': 'test1', 'pwd':'test'})

@app.route('/appname/module/rest/task/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    if len(task) == 0:
        return jsonify({"modid":"1234","name":"abcd","status":"alarm","remark":"good"})
    return jsonify({'task': task[0]})


if __name__ == '__main__':
    app.run(debug=True,host="10.56.56.236",port=65500)
