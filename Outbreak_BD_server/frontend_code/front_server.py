# coding=utf-8
from flask import Flask, jsonify, request,Flask,redirect
from flask import render_template
from process.hot import process_hot
from process.hot_default import process_hot_default
from process.predict import predict_lr
from process.map import process_map
from process.news import process_new
from process.statistics import process_statistics
import re
import json
import requests
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.url_map.strict_slashes = False  # Disable redirecting on POST method from /star to /star/
@app.route('/',methods=['GET','POST'])
def hot():
    if request.method == 'GET':
        # 可以通过 request 的 args 属性来获取参数
        name = request.args.get("name")
        size = request.args.get("size")
        if size:
            data = process_hot(size)
            return render_template('hot.html', li=data)
        else:
            data = process_hot_default()
            return render_template('hot.html', li=data)
@app.route('/map', methods=['GET','POST'])
def map():
    if request.method == 'GET':
        geo = process_map()
        return render_template('map.html', myechart=geo.render_embed())
@app.route('/timespace', methods=['GET','POST'])
def timespace():
    if request.method == 'GET':
        return render_template('timespace.html')
@app.route('/city', methods=['GET','POST'])
def city():
    if request.method == 'GET':
        return render_template('city.html')
# nlp部分
@app.route('/news', methods=['GET','POST'])
def news():
    # 使用循环展示内容
    if request.method == 'GET':
        # 默认20条信息
        news = process_new(size=20)
        # context = {
        #     'news': [
        #         {
        #             'name': '三国演义',
        #             'author': '罗贯中',
        #             'price': 110
        #         }, {
        #             'name': '西游记',
        #             'author': '吴承恩',
        #             'price': 109
        #         }
        #     ]
        # }
        return render_template('news.html', **news)
        # return render_template('news.html')
@app.route('/statistics', methods=['GET','POST'])
def statistics():
    # 城市对比图
    if request.method == 'GET':
        bar = process_statistics()
        return render_template('statistics.html', myechart=bar.render_embed())
@app.route('/predict', methods=['GET','POST'])
def predict():
    # 城市对比图
    if request.method == 'GET':
        #  lr model
        data = predict_lr()
        return render_template('predict.html', li=data)
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')
@app.errorhandler(500)
def not_found(error):
    return render_template('404.html')
if __name__ == '__main__':
    app.run()