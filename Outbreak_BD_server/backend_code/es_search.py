from dao.es_dao import es_connect
es = es_connect()
def seach_cont(index):
    doc_type = index
    resource = es.count(index=index, doc_type=doc_type)
    # 直接返回es_json 取数据
    return resource
def m_search(index,size):
    # 使用聚合查询
    query = {
        "query": {
            "match_all": {}
        },
        "sort": {"ct": {"order": "desc"}}
    }
    query = es.search(index=index,  body=query, size=size)
    return query

def m_search_news(index,size):
    # 使用聚合查询
    query = {
        "query": {"match_all": {}},
        "sort": {"id": {"order": "desc"}},
        "collapse": {"field": "id"}}
    query = es.search(index=index,  body=query, size=size)
    return query
# if __name__ == '__main__':
#     import time
#     st = time.time()
#     es = es_connect()
#     # index = 'outbreak_data_summary'
#     # size = 10
#     # print(m_search(index, size))
#     # 统计总数据
#     # print(seach_cont(index))
#     # province查询
#     # index = 'outbreak_data_country'
#     # size = 100
#     # print(m_search(index, size))
#     #
#     # # m_search_news
#     # 利用折可以直接将重复的值进行折叠
#     index = 'outbreak_data_news'
#     size = 30
#     print(m_search_news(index, size))
#     print('time used:{}'.format(time.time()-st))
