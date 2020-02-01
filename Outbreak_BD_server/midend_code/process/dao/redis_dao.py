# -*- coding: utf-8 -*
import redis
redis_client_pool = redis.ConnectionPool(host='localhost', port=6379, db=1, password='1234')
redis_client = redis.Redis(connection_pool=redis_client_pool)
def delete_result(name, key_):
    # 构建推荐列表
    status = redis_client.hdel(name, key_)
    return status
def predict_insert_(name, key_, value_):
    # hset_insert
    status = redis_client.hset(name, key_, value_)
    return status
def predict_insert_nx(name, key_, value_):
    # hsetnx_insert
    status = redis_client.hsetnx(name, key_, value_)
    return status
def predict_sadd(name, key_, value_):
    status = redis_client.sadd(name, key_, value_)
    return status
def redis_push(name, key_list):
    status = redis_client.lpush(name, key_list)
    return status
def redis_pop(name, key_):
    # hsetnx_insert
    status = redis_client.lpop(name)
    return status
def predict_get_value(name, key_):
    # search
    value = redis_client.hget(name, key_)
    return value
def madd(name, key_):
    # search
    value = redis_client.madd(name, key_)
    return value
def getall_value(name):
    all_value = redis_client.hvals(name)
    return all_value
def getall(name):
    # search
    all_ = redis_client.hgetall(name)
    return all_
def getall_keys(name):
    all_keys = redis_client.hkeys(name)
    return all_keys
def getall_keys_scan(name):
    keys = []
    for key_, value_ in redis_client.hscan_iter(name):
        keys.append(str(key_).strip().replace('\t', ''))
    return keys