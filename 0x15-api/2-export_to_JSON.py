#!/usr/bin/python3
"""Script that, using this REST API, for a given employee ID and
export data in the JSON format."""
from sys import argv
from urllib import request
import json
import urllib


if __name__ == "__main__":
    if len(argv) is 2 and argv[1].isdigit():
        with urllib.request.urlopen(
         'https://jsonplaceholder.typicode.com/users/{}'.
         format(argv[1])) as response:
            raw_data = response.read()
            encoding = response.info().get_content_charset('utf8')
            data = json.loads(raw_data.decode(encoding))
            userName = data.get('username')
        with urllib.request.urlopen(
         'https://jsonplaceholder.typicode.com/todos?userId={}'.
         format(argv[1])) as response:
            raw_data = response.read()
            encoding = response.info().get_content_charset('utf8')
            data = json.loads(raw_data.decode(encoding))
            taskes = len(data)
            l = []
            for dic in range(0, taskes):
                task = {}
                task['username'] = userName
                task['task'] = data[dic].get('title')
                task['completed'] = data[dic].get('completed')
                l.append(task)
            task_end = {}
            task_end[argv[1]] = l
            with open('{}.json'.format(argv[1]), 'w') as outfile:
                json.dump(task_end, outfile)
