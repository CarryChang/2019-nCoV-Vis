from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from es_search import m_search, m_search_news
import json
app = Flask(__name__)
api = Api(app)
# 返回的json支持中文
app.config['JSON_AS_ASCII'] = False
@app.route('/es_virus_data', methods=['POST'])
def hot():
    data = json.loads(request.get_data().decode('utf-8'))
    index = 'outbreak_data_summary'
    size = data['size']
    info = m_search(index, size)
    return jsonify(info)
@app.route('/es_virus_static', methods=['POST'])
def statics():
    data = json.loads(request.get_data().decode('utf-8'))
    index = 'outbreak_data_country'
    size = data['size']
    info = m_search(index, size)
    return jsonify(info)
@app.route('/es_virus_news', methods=['POST'])
def news():
    data = json.loads(request.get_data().decode('utf-8'))
    index = 'outbreak_data_news'
    size = data['size']
    info = m_search_news(index, size)
    return jsonify(info)
if __name__ == '__main__':
    app.run()