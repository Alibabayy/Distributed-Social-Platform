# ui.py

# Starter code for assignment 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# yiyang feng
# yiyangf2@uci.edu
# 66462506
def process_command(ans):
    command = ans[0]
    ans = ans.replace(ans[0], '', 1)
    if command == 'C':
        index = ans.find('-')
        option = ans[index] + ans[index + 1]
        ans_list = ans.split(option, 1)
        path = ans_list[0].strip(' ')
        for i in ans_list[1:]:
            option += i
        return (path, option)
    elif command == 'O':
        path = ans.strip(' ')
        return path
    elif command in ('E', 'P'):
        ans = ans.strip(' ').split('-')
        return ans