"Test the de_messenger.py"


from ds_messenger import DirectMessenger

IP = '168.235.86.101'
user1 = DirectMessenger(IP, 'ellasasaaa', 1232324351232111)
user2 = DirectMessenger(IP, 'nicolassasssa', 978263101)
user1.get_token()
user2.get_token()
user1.send("hi, for test", 'nicolassasssa')
test_message = user2.retrieve_all()
print(test_message)
