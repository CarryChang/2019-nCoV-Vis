import requests
import re
import json
from dao.es_dao import es_connect
es = es_connect()
def fuzzy_search(query_content,page,size):
    para = {'query_content': query_content, 'page': page, 'size': size}
    # 中台请求后台数据
    query = requests.post("http://localhost:8000/es_fuzzy_search", data=json.dumps(para)).json()
    # query = requests.post("http://175.24.69.6:8000/es_fuzzy_search", data=json.dumps(para)).json()
    province_detail = {}
    province_detail_all_list = []
    for i in query['hits']['hits']:
        # print(i)
        new_city = i['_source']['city']
        if '-' in new_city:
            # 清洗城市,拿到市区
            new_city = re.findall('(.*)-', new_city)[0]
        else: pass
        i['filter_city'] = new_city
        if new_city not in province_detail.keys():
            province_detail[new_city] = 0
            province_detail[new_city] += 1
        else:
            province_detail[new_city] += 1
    for key_city in province_detail.keys():
        province_detail_all = dict({'name': key_city, 'value': province_detail[key_city]})
        province_detail_all_list.append(province_detail_all)
    query['geographical_distribution'] = province_detail_all_list
    return query
# if __name__ == '__main__':
#     import time
#     st = time.time()
#     query_content = '代码'
#     page = 1
#     size = 10
#     print(fuzzy_search(query_content, page, size))
#     print('time used :{}'.format(time.time() - st))