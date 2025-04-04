"main program"
# a4.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# yiyang feng
# yiyangf2@uci.edu
# 66462506


import os
import unittest
from pathlib import Path
from LastFM import LastFM
from OpenWeather import OpenWeather
import Profile
from ui import process_command
import ds_client


class SimpleTest(unittest.TestCase):
    def test_OpenWeather(self):
        open_weather = OpenWeather("92697", "US")
        open_weather.set_apikey("67fcab5c53747315abd0075d15383708")
        open_weather.load_data()
        message = "@weather uuu @temperature"
        new_message = open_weather.transclude(message)
        assert '@weather' not in new_message and '@temperature' not in new_message
    
    def test_LastFM(self):
        lastfm = LastFM()
        lastfm.set_apikey("e1ecbf0790632af20d0df2b3c0519fdf")
        lastfm.load_data()
        message = '@album uuu @lastfm'
        new_message = lastfm.transclude(message)
        assert '@album' not in new_message and '@lastfm' not in new_message


class WrongCommandError(Exception):
    'test'


class NotCorrectDsu(Exception):
    'test'


class NotIntegerPort(Exception):
    'test'


def print_menu():
    "print the menu command"
    print('Now except C and O command, you have three more command (E, P and Q). Here are their functions')
    print('P -usr: Prints the username stored in the profile object')
    print('  -pwd: Prints the password stored in the profile object')
    print('  -bio: Prints the bio stored in the profile object')
    print('  -posts: Prints all posts stored in the profile object with their ID')
    print('  -post [ID]: Prints post identified by ID')
    print('  -all: Prints all content stored in the profile object')
    print('E -usr [USERNAME]: edit the usrename stored in the profile object')
    print('  -pwd [PASSWORD]: edit the password stored in the profile object')
    print('  -bio [BIO]: edit the bio stored in the profile object')
    print('  -addpost [NEW POST: add a new post into the posts stored in the profile object')
    print('  -delpost [ID]: delete the posts stored in the profile object with their ID')
    print('Q: quit the program')


def function_for_command_C():
    "function for command C"
    global profile1, p
    ff_name = option.replace('-n', '').strip(' ')
    extension = ff_name + '.dsu'
    file_name = os.path.join(path, extension)
    p = Path(file_name)
    if p.exists():
        ffff = open(p)
        profile1 = Profile.Profile()
        profile1.load_profile(file_name)
        print('the file you want to create is already exists. Now it is open for you')
    elif not p.exists():
        ffff = open(p, 'a')
        usernames = input("Please enter a unique name to associate the user with posts:\n")
        while ' ' in usernames:
            usernames = input('Please enter a username without empty spaces:\n')
        passwords = input("Please enter a password to protect access to user journal entries:\n")
        while ' ' in passwords:
            passwords = input('Please enter a password without empty spaces:\n')
        bio = input("Please enter a brief description of the user:\n")
        answer = input('Whether to post the bio online to the server? (yes/no):\n')
        while not answer in ('yes', 'no'):
            answer = input('Whether to post the bio online to the server? (yes/no):\n')
        profile1 = Profile.Profile(username=usernames, password=passwords)
        profile1.bio = bio
        profile1.dsuserver = server
        profile1.save_profile(p)
        if answer == 'yes':
            bio_post = Profile.Post(profile1.bio)
            an = ds_client.send(server, port, profile1.username, profile1.password, '', bio_post)
            if an is True:
                print('The message has been sent to the server')
            elif an is False:
                print('A Error occurs when connecting the server. The bio is not posted online.')


if __name__ == '__main__':
    server = input('Please enter the IP Address of the server you want to connect:\n').strip(' ')
    port = input('Please enter the port:\n')
    try:
        int(port)
    except:
        raise NotIntegerPort
    command = input("Welcome! Do you want to create or open a DSU file (type 'C' to create or 'O' to open):\n").strip(' ')
    if command == 'C':
        path = input("Great! What is the path of location you want to create the file:\n").strip(' ')
        name = input('Please enter the name of the new DSU file that you want to create:\n').strip(' ')
        option = '-n' + name
    elif command == 'O':
        path = input('Great! what is the path of DSU file you want to open:\n').strip()
    else:
        raise WrongCommandError
    count = 0
    while command != 'Q':
        if command == 'C':
            function_for_command_C()
        if command == 'O':
            p = Path(path)
            if p.suffix == '.dsu':
                ffff = open(p)
                profile1 = Profile.Profile()
                profile1.load_profile(path)
                print(f'{path} is open successfully')
            elif p.suffix != '.dsu':
                raise NotCorrectDsu
        elif command == 'E':
            ans = process_command(ans)
            for option in ans:
                if 'usr' in option:
                    new_att = option.replace('usr', '', 1).strip(' ')
                    if new_att != '':
                        profile1.username = new_att.replace('"', '').replace("'", '')
                        profile1.save_profile(p)
                elif 'pwd' in option:
                    new_att = option.replace('pwd', '', 1).strip(' ')
                    if new_att != '':
                        profile1.password = new_att.replace('"', '').replace("'", '')
                        profile1.save_profile(p)
                elif 'bio' in option:
                    new_att = option.replace('bio', '', 1).strip(' ')
                    if new_att != '':
                        profile1.bio = new_att.replace('"', '').replace("'", '')
                        profile1.save_profile(p)
                        answer = input('Whether to post the new bio online to the server? (yes/no):\n')
                        while not answer in ('yes', 'no'):
                            answer = input('Whether to post the bio online to the server? (yes/no):\n')
                        if answer == 'yes':
                            bio_post = Profile.Post(profile1.bio)
                            an = ds_client.send(server, port, profile1.username, profile1.password, '', bio_post)
                            if an is True:
                                print('The message has been sent to the server')
                            elif an is False:
                                print('A Error occurs when connecting the server. The bio is not posted online.')
                elif 'addpost' in option:
                    print('for the journal post, I could transclude these keywords into data from your API class')
                    print('@weather, @temperature, @lastfm, @album')
                    second_ans = input('Do you want to transclude these keywords?(yes/no)\n')
                    new_att = option.replace('addpost', '', 1).strip(' ')
                    if second_ans == 'yes':
                        open_weather = OpenWeather("92697", "US")
                        lastfm = LastFM()
                        open_weather.set_apikey("67fcab5c53747315abd0075d15383708")
                        open_weather.load_data()
                        new_att = open_weather.transclude(new_att)
                        lastfm.set_apikey("e1ecbf0790632af20d0df2b3c0519fdf")
                        lastfm.load_data()
                        new_att = lastfm.transclude(new_att)
                    if new_att != '':
                        post = Profile.Post(new_att.replace('"', '').replace("'", ''))
                        profile1.add_post(post)
                        profile1.save_profile(p)
                        answer = input('Whether to post the new post online to the server? (yes/no):\n')
                        while not answer in ('yes', 'no'):
                            answer = input('Whether to post the bio online to the server? (yes/no):\n')
                        if answer == 'yes':
                            an = ds_client.send(server, port, profile1.username, profile1.password, post)
                            if an is True:
                                print('The message has been sent to the server')
                            elif an is False:
                                print('A Error occurs when connecting the server. The post is not posted online.')
                elif 'delpost' in option:
                    new_att = option.replace('delpost', '', 1).strip(' ')
                    if new_att != '':
                        profile1.del_post(int(new_att.replace('"', '').replace("'", '')))
                        profile1.save_profile(p)
        elif command == 'P':
            ans = process_command(ans)
            for option in ans:
                if 'usr' in option:
                    print(profile1.username)
                elif 'pwd' in option:
                    print(profile1.password)
                elif 'bio' in option:
                    print(profile1.bio)
                elif 'posts' in option:
                    for i in range(len(profile1._posts)):
                        print(i, profile1._posts[i])
                elif 'post' in option:
                    id = option.replace('post', '', 1).strip(' ')
                    print(profile1._posts[int(id)])
                elif 'all' in option:
                    print('dsuserver =', profile1.dsuserver)
                    print('username =', profile1.username)
                    print('password =', profile1.password)
                    print('bio =', profile1.bio)
                    print('posts =', profile1._posts)
        elif not command in ('C', 'O', 'P', 'E', 'Q'):
            raise WrongCommandError
        if count == 0:
            print_menu()
            count = 1
        ans = input("Enter a new command:\n")
        command = ans[0]
        if command in ('C', 'O'):
            if command == 'C':
                server = input('Please enter the IP Address of the server you want to connect:\n').strip(' ')
                path = input("Great! What is the path of location you want to create the file:\n").strip(' ')
                name = input('Please enter the name of the new DSU file that you want to create:\n').strip(' ')
                option = '-n' + name
            elif command == 'O':
                path = input('Great! what is the path of DSU file you want to open:\n').strip()
