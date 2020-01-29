#!/user/bin/env python3
# -*- coding: utf-8 -*-
import requests
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
if __name__ == '__main__':
    import time
    from dao.es_dao import es_connect
    from datetime import datetime
    ct = datetime.now()
    es = es_connect()
    st = time.time()
    es_data = run_spider()
    index = 'outbreak_data'
    body = dict({"body": es_data, 'ct': ct})
    status = es.index(index=index, doc_type=index, body=body)
    print(status)
    print(ct)
    print('time used:{}'.format(time.time()-st))