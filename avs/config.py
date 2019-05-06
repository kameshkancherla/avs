# -*- coding: utf-8 -*-

import json
import os
import sys
import uuid

DEFAULT_CONFIG_FILE = os.path.join(os.path.expanduser('~'), '.avs.json')


def load(configfile=DEFAULT_CONFIG_FILE):
    if configfile is None:
        configfile = DEFAULT_CONFIG_FILE
        
    if not os.path.isfile(configfile):
        raise RuntimeError('No configuration file')

    with open(configfile, 'r') as f:
        config = json.load(f)
        require_keys = ['product_id', 'client_id', 'client_secret']
        for key in require_keys:
            if not ((key in config) and config[key]):
                raise RuntimeError('{} should include "{}"'.format(configfile, key))

    if ('host_url' not in config) or (not config['host_url']):
        config['host_url'] = 'avs-alexa-na.amazon.com'

    if config['host_url'] == 'dueros-h2.baidu.com':
        config['api'] = 'dcs/avs-compatible-v20160207'
        config['refresh_url'] = 'https://openapi.baidu.com/oauth/2.0/token'
    else:
        config['api'] = 'v20160207'
        config['refresh_url'] = 'https://api.amazon.com/auth/o2/token'

    return config


def save(config, configfile=None):
    if configfile is None:
        configfile = DEFAULT_CONFIG_FILE

    with open(configfile, 'w') as f:
        json.dump(config, f, indent=4)


def dueros():
    product_id = "xiaojing-" + uuid.uuid4().hex
    return {
        "dueros-device-id": product_id,
        "client_id": "lud6jnwdVFim4K4Zkoas3BkRVLvCO57Z",
        "host_url": "dueros-h2.baidu.com",
        "client_secret": "A017kke1GSSz7hp8Fj6ySoIWrnFraxf5",
        "product_id": product_id
    }

def alexa():
    return {
        "product_id": "rk322x",
        "client_id": "amzn1.application-oa2-client.03028146ba4a44b5bb31f0b4d0422251",
        "host_url": "avs-alexa-na.amazon.com",
        "client_secret": "47e089f9cb92256a55d76060d394328f762654d7c02165cb7f54757374d76219"
    }
