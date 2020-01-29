#!/user/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json
import re
from pyecharts import options as opts
from pyecharts.charts import Map
def dic_to_list(data_dict):
    provience_list = []
    max_list = []
    for key in data_dict.keys():
        value = data_dict[key]
        max_list.append(value)
        provience_list.append([key, value])
    return provience_list, max(max_list)
def process_map():
    para = {'size': 80}
    # print(para)
    data_source = requests.post("http://localhost:7000/es_virus_data", data=json.dumps(para)).json()
    # 得出地理信息/感染数量/
    confirmedCount_province_list = {}
    suspectedCount_province_list = {}
    curedCount_province_list = {}
    deadCount_province_list = {}
    for source in province_souce['hits']['hits']:
        base = source['_source']
        provinceShortName = base['provinceShortName']
        confirmedCount = base['confirmedCount']
        suspectedCount = base['suspectedCount']
        curedCount = base['curedCount']
        deadCount = base['deadCount']
        # print('{}-{}-{}-{}-{}'.format(provinceShortName,confirmedCount,suspectedCount,curedCount,deadCount))
        if provinceShortName not in confirmedCount_province_list.keys():
            confirmedCount_province_list[provinceShortName] = int(confirmedCount)
        if provinceShortName not in suspectedCount_province_list.keys():
            suspectedCount_province_list[provinceShortName] = int(suspectedCount)
        if provinceShortName not in curedCount_province_list.keys():
            curedCount_province_list[provinceShortName] = int(curedCount)
        if provinceShortName not in deadCount_province_list.keys():
            deadCount_province_list[provinceShortName] = int(deadCount)
    confirm_list, max_confirm = dic_to_list(confirmedCount_province_list)
    suspect_list, max_suspect = dic_to_list(suspectedCount_province_list)
    cure_list, max_cure = dic_to_list(curedCount_province_list)
    dead_list, max_dead = dic_to_list(deadCount_province_list)
    # list1 = [['山东', 526996], ['江苏', 458368], ['河北', 283797], ['浙江', 278097],
    #          ['上海市', 251175], ['天津市', 93933], ['陕西', 84043], ['河南', 79902]]
    # print('{}-{}-{}-{}'.format(max_confirm,max_dead,max_suspect,max_cure))
    geo = Map()
    geo.add('确诊', confirm_list)
    geo.add('疑似', suspect_list)
    geo.add('治愈', cure_list)
    geo.add('死亡', dead_list, maptype='china', is_map_symbol_show=True).set_series_opts(label_opts=opts.LabelOpts(is_show=True))\
        .set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=200, min_=0), title_opts=opts.TitleOpts(title='各地区疫情情况'))
    return geo
# if __name__ == '__main__':
#     import time
#     st = time.time()
#     process_map()
#     print('time used"{}'.format(time.time()-st))