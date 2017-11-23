#!/bin/python
# -*- coding:utf-8 -*-
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

tasks = [
	{"modid":"79600","name":"检查线路1","status":"未完成","remark":"2017/12/12 日截止"},
	{"modid":"79601","name":"添加设备2","status":"完成","remark":"2017/11/11 已结束"}
	]
#json_data = [
#{"tasks":("10001","123", "234", "79600", "79601")},
#{"modid":"10001","name":"完成flask主站","status":"完成","remark":"2017/11/23已结束"},
#{"modid":"123","name":"abc","status":"ok","remark":"good"},
#{"modid":"234","name":"bcd","status":"nook","remark":"needtocheck"},
#        {"modid":"79600","name":"检查线路1","status":"未完成","remark":"2017/12/12日截止"},
#        {"modid":"79601","name":"添加设备2","status":"完成","remark":"2017/11/11已结束"}

#]

with open("./record.json",'r') as load_f:
	json_data = json.load(load_f)

@app.route('/appname/module/rest/task', methods=['GET', 'POST'])
def tasks():
    if request.method == 'POST':
	json_data.append(request.json)
	json_data[0].setdefault("tasks",[ ]).append(request.json['modid'])
        return jsonify({'task': 'ok'}), 201
    else:
        return jsonify(json_data[0])

@app.route('/appname/module/rest/user', methods=['GET'])
def get_user():
    return jsonify({'user': 'test1', 'pwd':'test'})

@app.route('/appname/module/rest/task/<int:task_id>', methods=['GET'])
def get_task(task_id):
    return jsonify(json_data[task_id])


if __name__ == '__main__':
    app.run(debug=True,host="10.56.56.236",port=65500)
