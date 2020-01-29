from dao.es_dao import es_connect
import json
def creat_index():
    for index in ['outbreak_data', 'outbreak_data_news', 'outbreak_data_country', 'outbreak_data_summary']:
        print(es.indices.delete(index=index, ignore=[400, 404]))
def del_index():
    for index in ['outbreak_data', 'outbreak_data_news', 'outbreak_data_country', 'outbreak_data_summary']:
        print(es.indices.create(index=index, ignore=[400, 404]))
if __name__ == '__main__':
    # 给出插入信息
    es = es_connect()
    del_index()
    creat_index()
