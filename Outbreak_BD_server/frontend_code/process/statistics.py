#!/user/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json
import re
from pyecharts import options as opts
from pyecharts.charts import Bar,Line
def dic_to_list(data_dict):
    provience_list = []
    max_list = []
    for key in data_dict.keys():
        value = data_dict[key]
        max_list.append(value)
        provience_list.append([key, value])
    return provience_list, max(max_list)
def process_statistics():
    para = {'size': 80}
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
    provinces = list(confirmedCount_province_list.keys())
    confirm_list = list(confirmedCount_province_list.values())
    suspect_list = list(suspectedCount_province_list.values())
    cure_list = list(curedCount_province_list.values())
    dead_list = list(deadCount_province_list.values())
    # bar = Line()
    bar = Bar()
    bar.add_xaxis(provinces)
    bar.add_yaxis("确诊", confirm_list, stack="stack1")
    bar.add_yaxis("疑似", suspect_list, stack="stack1")
    bar.add_yaxis("治愈", cure_list, stack="stack1")
    bar.add_yaxis("死亡", dead_list, stack="stack1")
    bar.set_series_opts(label_opts=opts.LabelOpts(is_show=True))
    bar.set_global_opts(title_opts=opts.TitleOpts(title="省份疫情统计"))
    return bar
# if __name__ == '__main__':
#     process_statistics()