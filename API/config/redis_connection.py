#!/usr/bin/python
# -*- encoding: utf-8 -*-

import os

# class BaseConfig(object):
#     CACHE_TYPE = os.environ['CACHE_TYPE']
#     CACHE_REDIS_HOST = os.environ['CACHE_REDIS_HOST']
#     CACHE_REDIS_PORT = os.environ['CACHE_REDIS_PORT']
#     CACHE_REDIS_DB = os.environ['CACHE_REDIS_DB']
#     CACHE_REDIS_URL = os.environ['CACHE_REDIS_URL']
#     CACHE_DEFAULT_TIMEOUT = os.environ['CACHE_DEFAULT_TIMEOUT']

class BaseConfig(object):
    CACHE_TYPE = 'redis' 
    CACHE_REDIS_HOST = '144.22.139.197' 
    CACHE_REDIS_PORT = '6379'
    CACHE_REDIS_DB = 0