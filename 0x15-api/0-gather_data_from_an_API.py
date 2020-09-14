#!/usr/bin/python3
"""Script that, using this REST API, for a given employee ID, returns
information about his/her to list progress."""
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
            name = data.get('name')
        with urllib.request.urlopen(
         'https://jsonplaceholder.typicode.com/todos?userId={}'.
         format(argv[1])) as response:
            raw_data = response.read()
            encoding = response.info().get_content_charset('utf8')
            data = json.loads(raw_data.decode(encoding))
            l = []
            taskes = len(data)
            for dic in range(0, taskes):
                if data[dic].get('completed') is True:
                    l.append(data[dic].get('title'))
        print('Employee {} is done with tasks({}/{}):'
              .format(name, len(l), taskes))
        for i in l:
            print("\t {}".format(i))
