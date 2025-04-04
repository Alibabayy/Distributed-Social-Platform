# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# yiyang feng
# yiyangf2@uci.edu
# 66462506

import socket
import json
import ds_protocol

def send(server:str, port:int, username:str, password:str, message:str, bio:str=None):
  '''
  The send function joins a ds server and sends a message, bio, or both

  :param server: The ip address for the ICS 32 DS server.
  :param port: The port where the ICS 32 DS server is accepting connections.
  :param username: The user name to be assigned to the message.
  :param password: The password associated with the username.
  :param message: The message to be sent to the server.
  :param bio: Optional, a bio for the user.
  '''
  #TODO: return either True or False depending on results of required operation
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    try:
      int(port)
    except:
      return False
    client.connect((server, int(port)))
    mydict = {"username": username, "password": password, "token": ""}
    new_dict = {"join": mydict}
    join_msg = json.dumps(new_dict)
    send = client.makefile('w')
    recv = client.makefile('r')
    
    send.write(join_msg + '\r\n')
    send.flush()

    resp_j = recv.readline().strip('\r\n').strip(' ')
    resp = ds_protocol.extract_json(resp_j)
    # DataTuple(type='ok', message='Welcome to the ICS 32 Distributed Social!', token='e649985a-f79d-40f7-8f13-1a4a25948656')
    if resp != None:
      print(resp.message)
      token = resp.token
      if bio != None:
        dic = {'token': token, 'bio': bio}
        json_msg = json.dumps(dic)
        send.write(json_msg + '\r\n')
        send.flush()
      elif bio == None:
        dic = {'token': token, 'post': message}
        json_msg = json.dumps(dic)
        send.write(json_msg + '\r\n')
        send.flush()
      return True
    elif resp == None:
      return False
    