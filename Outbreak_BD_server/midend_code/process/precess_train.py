#!/user/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json
import re
import pytz
import datetime
import time
from dao.redis_dao import predict_insert_
from sklearn.linear_model import LinearRegression
def change_int(timestamp):
    # timestamp = timestamp/1000
    # 转换成localtime
    # time_local = time.localtime(timestamp)
    # dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    dt = datetime.datetime.fromtimestamp(timestamp, pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')
    return dt
def train_lr():
    para = {'size': 1500}
    data_source = requests.post("http://localhost:7000/es_virus_data", data=json.dumps(para)).json()
    c_time = []
    modifyTime = []
    confirmed = []
    suspect = []
    cure = []
    dead = []
    for data_list in data_source['hits']['hits']:
        base_info = data_list['_source']
        # c_time.append(base_info['ct'])
        # base_info_1 = str(base_info['body']['countRemark'])
        base_info_2 = base_info['body']
        modifyTime.append([int(base_info_2['modifyTime']/1000)])
        try:
            try:
                confirmed.append(base_info_2['confirmedCount'])
                suspect.append(base_info_2['suspectedCount'])
                cure.append(base_info_2['curedCount'])
                dead.append(base_info_2['deadCount'])
            except:
                base_info_1 = str(base_info_2['countRemark'])
                if '其中' not in base_info_1:
                    confirmed.append(int(re.findall('确诊(.*?)例', base_info_1)[0]))
                    suspect.append(int(re.findall('疑似(.*?)例', base_info_1)[0]))
                    cure.append(int(re.findall('治愈(.*?)例', base_info_1)[0]))
                    dead.append(int(re.findall('死亡(.*?)例', base_info_1)[0]))
                else:
                    confirmed.append(int(re.findall('确诊 (.*?)例', base_info_1)[0]))
                    suspect.append(int(re.findall('疑似 (.*?) 例', base_info_1)[0]))
                    cure.append(int(re.findall('治愈 (.*?) 例', base_info_1)[0]))
                    dead.append(int(re.findall('死亡 (.*?) 例', base_info_1)[0]))
        except:
            dead.append(41)
    data_source = dict({'modifyTime': modifyTime, 'confirmed': confirmed, 'dead': dead, 'suspect': suspect, 'cure': cure})
    print(len(data_source['modifyTime']))
    print(len(data_source['confirmed']))
    print(len(data_source['dead']))
    print(len(data_source['suspect']))
    print(len(data_source['cure']))
    # train and import lr
    predict_time_line_int = []
    predict_time_line = []
    now = int(time.time())
    for time_skip in range(0, 500000, 200):
    # for time_skip in range(0, 100, 20):
        predict_time_line_int.append([now + time_skip])
        predict_time_line.append(change_int(now + time_skip))
    # print(predict_time_line)
    data_predict = {}
    name, redis_key = 'ncov_lr_predict', 'predict_result'
    for key_ in ['confirmed', 'suspect', 'dead', 'cure']:
        lr_model = LinearRegression()
        # 使用hset进行覆盖
        lr_model.fit(data_source['modifyTime'], data_source[key_])
        # 预测本地时间之后，加入回归模型，并将结果存储到redis
        print('{} predict...'.format(key_))
        dict_name = '{}_list'.format(key_)
        data_predict[dict_name] = [int(result) for result in lr_model.predict(predict_time_line_int)]
    data_predict['predict_timeline'] = predict_time_line
    status = predict_insert_(name, redis_key, data_predict)
    print(status)
if __name__ == '__main__':
    st = time.time()
    '''通过回归模型去预测数据，时间和感染数目进行预测'''
    train_lr()
    print('time used:{}'.format(time.time()-st))