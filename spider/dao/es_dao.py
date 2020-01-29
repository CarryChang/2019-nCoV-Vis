#!/user/bin/env python3
# -*- coding: utf-8 -*-
def es_connect():
    import elasticsearch
    # es = elasticsearch.Elasticsearch([{'host': '', 'port': 9200, "http_auth": ('elastic', 'Elastic1024')}])
    es = elasticsearch.Elasticsearch([{'host': '175.24.69.6', 'port': 9200, "timeout": 30}])
    return es
# print(es_connect())