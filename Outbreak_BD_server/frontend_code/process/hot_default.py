#!/user/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json
import re
def process_hot_default():
    para = {'size': 200}
    data_source = requests.post("http://localhost:7000/es_virus_data", data=json.dumps(para)).json()
    c_time = []
    confirmed = []
    suspect = []
    cure = []
    dead = []
    for data_list in data_source['hits']['hits']:
        base_info = data_list['_source']
        c_time.append(base_info['ct'])
        base_info_1 = str(base_info['body']['countRemark'])
        try:
            try:
                base_info_2 = base_info['body']
                confirmed.append(base_info_2['confirmedCount'])
                suspect.append(base_info_2['suspectedCount'])
                cure.append(base_info_2['curedCount'])
                dead.append(base_info_2['deadCount'])
            except:
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
        except:pass
    data = dict({'time': c_time, 'title': '新型冠状病毒感染情况时间序列', 'confirmed': confirmed, 'dead': dead, 'suspect': suspect,'cure': cure})
    return data