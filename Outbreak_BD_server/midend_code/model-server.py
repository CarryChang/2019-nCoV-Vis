from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from process.mid_es_fuzzy_search import fuzzy_search
import requests
import json
app = Flask(__name__)
api = Api(app)
# 返回的json支持中文
app.config['JSON_AS_ASCII'] = False
@app.route('/mid_es_fuzzy_search', methods=['POST'])
def post():
    data = json.loads(request.get_data().decode('utf-8'))
    query_content = data['query_content']
    page = data['page']
    size = data['size']
    info = fuzzy_search(query_content, page, size)
    return jsonify(info)
if __name__ == '__main__':
    app.run(host='0.0.0.0')