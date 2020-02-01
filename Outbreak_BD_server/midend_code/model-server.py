from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import requests
import redis
import json
app = Flask(__name__)
api = Api(app)
# 返回的json支持中文
app.config['JSON_AS_ASCII'] = False
redis_client_pool = redis.ConnectionPool(host='localhost', port=6379, db=1, password='1234')
redis_client = redis.Redis(connection_pool=redis_client_pool)
def predict_get_value(name, key_):
    # search
    value = redis_client.hget(name, key_)
    return value
def get_lr_result(redis_name, redis_key):
    return eval(predict_get_value(redis_name, redis_key).decode())
@app.route('/ncov_lr_predict', methods=['POST'])
def post():
    data = json.loads(request.get_data().decode('utf-8'))
    redis_name = data['redis_name']
    redis_key = data['redis_key']
    info = get_lr_result(redis_name, redis_key)
    return jsonify(info)
if __name__ == '__main__':
    app.run()