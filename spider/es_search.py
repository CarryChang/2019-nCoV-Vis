from dao.es_dao import es_connect
def m_search(index):
    # match某一个数据
    # query = {
    #     "query": {
    #         "match": {
    #             "job_description": "机器学习"
    #         }
    #     }
    # }
    # # multi_match:在name和addr里匹配包含深圳关键字的数据，混合模糊查询
    # query = {
    #     "query": {
    #         "multi_match": {
    #             "query": "深圳",
    #             "fields": ["city"], "fuzziness": "AUTO",
    #         }
    #     }
    # }
    # 使用聚合查询
    # query = {
    #     "query": {
    #         "match_all": {}
    #     }
    # }
    # query ={
    #     "query": {
    #         "match": {
    #             "city": '*'
    #         }
    #     }
    # }
    doc_type = 'outbreak_data_summary'
    data = es.search(index=index)
    print(data)
    # query = es.search(index=index,  body=query)
    # return query
def seach_cont(index):
    doc_type = index
    resource = es.count(index=index, doc_type=doc_type,  ignore=[400, 404])
    # 直接返回es_json 取数据
    return resource
if __name__ == '__main__':
    import time
    st = time.time()
    es = es_connect()
    index = 'outbreak_data'
    print(m_search(index))
    # 统计总数据
    # print(seach_cont(index))
    print('time used :{}'.format(time.time() - st))