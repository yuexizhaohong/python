#!/usr/bin/env python

from generic import DefaultService

class cpu(DefaultService):
    name = 'cpu'
    interval = 60
    plugin_name = 'cpu_info'
    triggers = {
        'iowait':['percentage',5.5,90],
        'system':['percentage',5,90],
        'idle':['percnetage',20,10],
        'user':['percnetage',80,90],
        'steal':['percnetage',80,90],
        'nice':[None,80,90],
    }
    lt_operator = []

class memory(DefaultService):
    name = 'memory'
    plugin_name = 'mem_info'
    triggers = {
        'SwapUsage_p':['percnetage',66,91],
        'MemUsage_p':['percentage',68,92],
        'MemUsage':[None,60,65],
    }
 
class load(DefaultService):
    name = 'load'
    interval = 120
    plugin_name = 'load_info'
    triggers = {
        'load1':[int,4,9],
        'load5':[int,3,7],
        'load15':[int,3,9],
    }
