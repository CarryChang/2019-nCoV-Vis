from dao.es_dao import es_connect
import re
import json
def m_search(index):
    # match某一个数据
    query = {"query": {"match_all": {}}}
    query = es.search(index=index, body=query, size=1, ignore=[400, 404])
    return query
def transformer_data(data_source):
    # 通用清洗方案
    transfor_data = json.loads(re.findall(' = (.*)}catch', data_source)[0])
    return transfor_data
def transformer(data_list):
    for data_source in data_list:
        base = data_source['_source']
        ct = base['ct']
        body = base['body']
        source_news = {}
        source_news['_index'] = index
        source_news['_type'] = index
        source_news['_source'] = body
        getTimelineService = BeautifulSoup(body,'lxml').find_all(id="getTimelineService")
        action_news = transformer_data(str(getTimelineService))['result']
        status = helpers.bulk(es, action_news, ignore=[400, 404])
        print(' ')
        getListByCountryTypeService1 = BeautifulSoup(body,'lxml').find_all(id="getListByCountryTypeService1")
        print(transformer_data(str(getListByCountryTypeService1)))
        print(' ')
        getStatisticsService = BeautifulSoup(body, 'lxml').find_all(id="getStatisticsService")
        print(transformer_data(str(getStatisticsService)))
if __name__ == '__main__':
    import time
    import re
    from elasticsearch import helpers
    from bs4 import BeautifulSoup
    st = time.time()
    # 使用个性化推荐
    es = es_connect()
    index = 'outbreak_data'
    data_list = m_search(index)['hits']['hits']
    transformer(data_list)
    # 统计计数
    # print(seach_cont(index))
    print('time used :{}'.format(time.time() - st))