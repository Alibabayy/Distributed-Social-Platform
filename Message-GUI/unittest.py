"Test the ds_protocol.py"

import json
import unittest
from ds_protocol import extract_json


class test_function(unittest.TestCase):
    def test_message(self):
        mydict = {"type": "ok", "message": "Direct message sent"}
        dict = {'response': mydict}
        json_obj = json.dumps(dict)
        result = extract_json(json_obj)
        self.assertEqual(result.type, "ok")
        self.assertEqual(result.message, "Direct message sent")
    
    def test_messages(self):
        mydict = {"type": "ok", "messages": [{"message":"Hello User 1!", "from":"markb", "timestamp":"1603167689.3928561"},{"message":"Bzzzzz", "from":"thebeemoviescript", "timestamp":"1603167689.3928561"}]}
        dict = {'response': mydict}
        json_obj = json.dumps(dict)
        result = extract_json(json_obj)
        self.assertEqual(result.type, "ok")
        self.assertEqual(result.message, [{"message":"Hello User 1!", "from":"markb", "timestamp":"1603167689.3928561"},{"message":"Bzzzzz", "from":"thebeemoviescript", "timestamp":"1603167689.3928561"}])

    def test_mess(self):
        mydict = {"type": "ok", "message": "", "token":"12345678-1234-1234-1234-123456789abc"}
        dict = {'response': mydict}
        json_obj = json.dumps(dict)
        result = extract_json(json_obj)
        self.assertEqual(result.type, "ok")
        self.assertEqual(result.message, "")
        self.assertEqual(result.token, "12345678-1234-1234-1234-123456789abc")

if __name__ == '__main__':
    unittest.main()