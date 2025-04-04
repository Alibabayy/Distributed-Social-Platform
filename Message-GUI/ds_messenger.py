"send direct message"


import socket
import json
import time
from ds_protocol import extract_json


class WrongTokenError(Exception):
    "error class"


class DirectMessage:
    "Direct Message class"
    def __init__(self):
        self.recipient = None
        self.message = None
        self.timestamp = None


class DirectMessenger:
    "Direct Messenger class"
    def __init__(self, dsuserver=None, username=None, password=None):
        self.token = None
        self.dsuserver = dsuserver
        self.username = username
        self.password = password
        self.new_message = []
        self.sent_message = []

    def get_token(self):
        "firstly get the token by sending join message"
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((self.dsuserver, 3021))
            mydict = {"username": self.username, "password": self.password, "token": ""}
            new_dict = {"join": mydict}
            join_msg = json.dumps(new_dict)
            send = client.makefile('w')
            recv = client.makefile('r')
            send.write(join_msg + '\r\n')
            send.flush()
            resp_j = recv.readline().strip('\r\n').strip(' ')
            resp = extract_json(resp_j)
            if resp is not None:
                print(resp.message)
                self.token = resp.token

    def send(self, message: str, recipient: str) -> bool:
        # must return true if message successfully sent, false if send failed.
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((self.dsuserver, 3021))
            if self.token is None:
                raise WrongTokenError
            class_obj = DirectMessage()
            class_obj.recipient = recipient
            class_obj.message = message
            class_obj.timestamp = time.time()
            mess = {"entry": class_obj.message, "recipient": class_obj.recipient, "timestamp": class_obj.timestamp}
            dictt = {"token": self.token, "directmessage": mess}
            json_msg = json.dumps(dictt)
            send = client.makefile('w')
            recv = client.makefile('r')
            send.write(json_msg + '\r\n')
            send.flush()
            resp_j = recv.readline().strip('\r\n').strip(' ')
            resp = extract_json(resp_j)
            if resp is not None:
                print(resp.message)
                return True
            elif resp is None:
                return False

    def retrieve_new(self) -> list:
        "new funtion"
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((self.dsuserver, 3021))
            if self.token is None:
                raise WrongTokenError
            dictt = {"token": self.token, "directmessage": "new"}
            json_msg = json.dumps(dictt)
            send = client.makefile('w')
            recv = client.makefile('r')
            send.write(json_msg + '\r\n')
            send.flush()
            resp_j = recv.readline().strip('\r\n').strip(' ')
            resp = extract_json(resp_j)
            return resp.message

    def retrieve_all(self) -> list:
        "all function"
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((self.dsuserver, 3021))
            if self.token is None:
                raise WrongTokenError
            dictt = {"token": self.token, "directmessage": "all"}
            json_msg = json.dumps(dictt)
            send = client.makefile('w')
            recv = client.makefile('r')
            send.write(json_msg + '\r\n')
            send.flush()
            resp_j = recv.readline().strip('\r\n').strip(' ')
            resp = extract_json(resp_j)
            return resp.message
