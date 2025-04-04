At the beginning of the program, the program would ask users the IP Address of the server, port and command ('C' for creating a DSU file or 'O' for opening a DSU file)

if the command is 'C', it would ask users path of the folder to create the new file and the name of the new file
elif the command is 'O', it would only ask the path of the file user want to open

And then it would enter a while loop to excute the functions of different commands until users type 'Q' to exit the program

if the command is 'C',  it would uses function_for_commandC() function:
  it would open the file if the file has already existed
  if the file does not exist:
  it would create the file and ask for username, password and bio and then it would stored them and server in a object called profile1 using class
  And then it would ask whether to post the bio that user enter online to the server
  if user answers yes, it would import the ds_client to send the bio message using class Post in the form of json message to the server

How ds_client works:
   It would connect to the server with specific IP address and port
   And then it would firstly send join message to the server and receive a message back
   if the message sent back said "error", it would return False and tell the user the message would not be sent to the server further
   elif the message sent back said "ok", it would take two actions according to the parameter entered:
        if the user want to send the new bio message to the server, the bio parameter would be the new message and it would send it to the server
        if the user want to send the new post message by using addpost command, the bio parameter would be None and it would send the message stored in the message parameter to the server
 

if the command is 'O', it would open and load the file for the users

if the command is 'E':
  it would edit the username, password, bio and post in the profile1 and save it to the file according to the users' command ('usr', 'pwd', 'bio', 'addpost' and 'delpost')
  for the 'bio' command, after editing the bio, the program would ask whether to post the new bio to the server
    if user answers yes, it would import the ds_client to send the new bio message using class Post to the server
  for the 'addpost' command, after adding the post that the user input, it would ask whether to post it to the server
     if user answers yes, it would import the ds_client to send the post message  to the server

if the command is 'P':
  it would print the username, password, bio and post according to different commands

After each loop in while loop, the program would ask a new command until user enter 'Q'
And if the new command is 'C', it would ask users a new IP Addresss of the server and other things