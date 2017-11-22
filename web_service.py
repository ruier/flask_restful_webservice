#!/bin/python
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

tasks = [
	{"modid":"123","name":"abc","status":"ok","remark":"good"},
	{"modid":"111","name":"aaa","status":"ok","remark":"good"}
	]
json_data = [
{"tasks":("123")},
{"modid":"123","name":"abc","status":"ok","remark":"good"},
]
@app.route('/appname/module/rest/task', methods=['GET', 'POST'])
def tasks():
    if request.method == 'POST':
        return jsonify({'task': 'ok'}), 201
    else:
        return jsonify(json_data[0])

@app.route('/appname/module/rest/user', methods=['GET'])
def get_user():
    return jsonify({'user': 'test1', 'pwd':'test'})

@app.route('/appname/module/rest/task/1', methods=['GET'])
def get_task():
    return jsonify(json_data[1])


if __name__ == '__main__':
    app.run(debug=True,host="10.56.56.236",port=65500)
