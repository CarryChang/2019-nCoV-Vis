#!/user/bin/env python3
# -*- coding: utf-8 -*-
def es_connect():
    import elasticsearch
    es = elasticsearch.Elasticsearch([{'host': 'localhost', 'port': 9200, "http_auth": ('elastic', 'Elastic1024')}])
    return es
# print(es_connect())