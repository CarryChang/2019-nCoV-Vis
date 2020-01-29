#!/user/bin/env python3
# -*- coding: utf-8 -*-
import requests
from dao.es_dao import es_connect
import re
import json
def transformer_data(data_source):
    # 通用清洗方案
    transfor_data = json.loads(re.findall(' = (.*)}catch', data_source)[0])
    return transfor_data
def run_spider():
    url = 'http://3g.dxy.cn/newh5/view/pneumonia?from=singlemessage&isappinstalled=0'
    headers = {
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding":"gzip, deflate, br",
        "accept-language":"zh-CN,zh;q=0.9",
        "cache-control":"max-age=0",
        "if-modified-since":"Thu, 23 Jan 2020 01:56:04 GMT",
        "sec-fetch-mode":"navigate",
        "sec-fetch-site":"none",
        "sec-fetch-user":"?1",
        "upgrade-insecure-requests":"1",
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36",}
    data_source = requests.get(url, headers=headers).content.decode('utf-8')
    return data_source
def transformer(content):
    # extract news
    Timeline_news = []
    base_info = BeautifulSoup(content, 'lxml')
    getTimelineService = base_info.find_all(id="getTimelineService")
    for action_news1 in transformer_data(str(getTimelineService)):
        source_news = {}
        source_news['_index'] = 'outbreak_data_news'
        source_news['_type'] = 'outbreak_data_news'
        action_news1['ct'] = ct
        source_news['_source'] = action_news1
        Timeline_news.append(source_news)
    new_status = helpers.bulk(es, Timeline_news, ignore=[400, 404])
    print(new_status)
    # extract country
    CountryTypeService = []
    getListByCountryTypeService1 = base_info.find_all(id="getListByCountryTypeService1")
    for action_Country in transformer_data(str(getListByCountryTypeService1)):
        source_country = {}
        source_country['_index'] = 'outbreak_data_country'
        source_country['_type'] = 'outbreak_data_country'
        action_Country['ct'] = ct
        source_country['_source'] = action_Country
        CountryTypeService.append(source_country)
    new_status = helpers.bulk(es, CountryTypeService, ignore=[400, 404])
    print(new_status)
    # extract summary
    getStatisticsService = base_info.find_all(id="getStatisticsService")
    es_data = transformer_data(str(getStatisticsService))
    index = 'outbreak_data_summary'
    doc_type = 'outbreak_data_summary'
    body_source = dict({"body": es_data, 'ct': ct})
    status = es.index(index=index, doc_type=doc_type, body=body_source)
    print(status)

if __name__ == '__main__':
    import time
    from datetime import datetime
    from bs4 import BeautifulSoup
    from elasticsearch import helpers
    ct = datetime.now()
    es = es_connect()
    st = time.time()
    data_source = run_spider()
    transformer(data_source)
    print(ct)
    print('time used:{}'.format(time.time()-st))