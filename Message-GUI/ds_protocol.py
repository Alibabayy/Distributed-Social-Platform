"protocol module"
# ds_protocol.py
# Replace the following placeholders with your information.

# yiyang feng
# yiyangf2@uci.edu
# 66462506

import json
from collections import namedtuple


DataTuple = namedtuple('DataTuple', ['type', 'message', 'token'])
DataTuple2 = namedtuple('Datatuple2', ['type', 'message'])


def extract_json(json_msg: str) -> DataTuple:
    '''
    json.loads function on a json string, convert it to a DataTuple object
    '''
    try:
        json_obj = json.loads(json_msg)
        if len(json_obj['response']) == 3:
            type = json_obj['response']['type']
            message = json_obj['response']['message']
            token = json_obj['response']['token']
            return DataTuple(type, message, token)
        if len(json_obj['response']) == 2:
            try:
                type = json_obj['response']['type']
                message = json_obj['response']['message']
            except KeyError:
                messages = json_obj['response']['messages']
                return DataTuple2(type, messages)
    except json.JSONDecodeError:
        print("Json cannot be decoded.")
    if type == 'ok':
        return DataTuple2(type, message)
    if type == 'error':
        print(message)
