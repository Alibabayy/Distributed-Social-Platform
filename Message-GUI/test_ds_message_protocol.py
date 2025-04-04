"Test the ds_protocol.py"

import json
from ds_protocol import extract_json


def test_message():
    "test message response"
    mydict = {"type": "ok", "message": "Direct message sent"}
    mydict = {'response': mydict}
    json_obj = json.dumps(mydict)
    result = extract_json(json_obj)
    return result


def test_messages():
    "test messages response"
    mydict = {"type": "ok", "messages": [{"message": "Hello User 1!", "from": "markb", "timestamp": "1603167689.3928561"}, {"message": "Bzzzzz", "from": "thebeemoviescript", "timestamp": "1603167689.3928561"}]}
    mydict = {'response': mydict}
    json_obj = json.dumps(mydict)
    result = extract_json(json_obj)
    return result


message = test_message()
print(message)
assert message.type == 'ok'
assert message.message == "Direct message sent"
messages = test_messages()
print(messages)
assert messages.type == 'ok'
assert messages.message == [{"message": "Hello User 1!", "from": "markb", "timestamp": "1603167689.3928561"}, {"message": "Bzzzzz", "from": "thebeemoviescript", "timestamp": "1603167689.3928561"}]
