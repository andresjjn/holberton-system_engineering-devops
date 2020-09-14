#!/usr/bin/python3
"""Script that, using this REST API, for a all employees and
export data in the JSON format."""
from sys import argv
import json
import urllib
from urllib import request


if __name__ == "__main__":

    with urllib.request.urlopen(
     'https://jsonplaceholder.typicode.com/users/') as response:
        raw_data = response.read()
        encoding = response.info().get_content_charset('utf8')
        data = json.loads(raw_data.decode(encoding))
        counter_users = len(data)
    users = {}
    for user in range(1, counter_users + 1):
        with urllib.request.urlopen(
         'https://jsonplaceholder.typicode.com/users/{}'.
         format(user)) as response:
            raw_data = response.read()
            encoding = response.info().get_content_charset('utf8')
            data = json.loads(raw_data.decode(encoding))
            users[user] = data.get('username')
    with urllib.request.urlopen(
     'https://jsonplaceholder.typicode.com/todos') as response:
        raw_data = response.read()
        encoding = response.info().get_content_charset('utf8')
        data = json.loads(raw_data.decode(encoding))
        for element in range(1, counter_users + 1):
            dics = []
            for task in data:
                if task.get('userId') is element:
                    dics_2 = {}
                    dics_2['completed'] = task.get('completed')
                    dics_2['task'] = task.get('title')
                    dics_2['username'] = users[element]
                    dics.append(dics_2)
            users[element] = dics
    with open('todo_all_employees.json', mode='w', encoding='utf-8') as output:
        json.dump(users, output)
