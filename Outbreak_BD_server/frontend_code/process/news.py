#!/user/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json
import re
import pytz
import datetime
import time
def change_time(timestamp):
    timestamp = timestamp/1000
    # 转换成localtime
    time_local = time.localtime(timestamp)
    # dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    dt = datetime.datetime.fromtimestamp(timestamp, pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')
    return dt
def process_new(size):
    para = {'size': size}
    data_source = requests.post("http://localhost:7000/es_virus_data", data=json.dumps(para)).json()
    news = []
    context = {}
    for data_list in data_source['hits']['hits']:
        base_info = data_list['_source']
        infoSource = base_info['infoSource']
        pubDate = change_time(base_info['pubDate'])
        sourceUrl = base_info['sourceUrl']
        title = base_info['title']
        summary = base_info['summary']
        try:
            provinceName = base_info['provinceName']
        except:
            provinceName = '国外'
        # print('{}-{}-{}-{}-{}-{}'.format(infoSource,pubDate,sourceUrl,title,summary,provinceName))
        data = dict({'infoSource': infoSource,
                     'title': title, 'pubDate': pubDate,
                     'sourceUrl': sourceUrl, 'summary': summary,'provinceName':provinceName})
        news.append(data)
    context['news'] = news
    return context

# if __name__ == '__main__':
#     import time
#     st = time.time()
#     size = 10
#     print(process_new(size))
#
#     print(time.time()-st)