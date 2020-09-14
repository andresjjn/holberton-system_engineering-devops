#!/usr/bin/python3
"""Script that, using this REST API, for a given employee ID, and
export data in the CSV format."""
import csv
import json
from sys import argv
import urllib
from urllib import request


if __name__ == "__main__":
    if len(argv) is 2 and argv[1].isdigit():
        with urllib.request.urlopen(
         'https://jsonplaceholder.typicode.com/users/{}'
         .format(argv[1])) as response:
            raw_data = response.read()
            encoding = response.info().get_content_charset('utf8')
            data = json.loads(raw_data.decode(encoding))
            userName = data.get('username')
        with urllib.request.urlopen(
         'https://jsonplaceholder.typicode.com/todos?userId={}'
         .format(argv[1])) as response:
            raw_data = response.read()
            encoding = response.info().get_content_charset('utf8')
            data = json.loads(raw_data.decode(encoding))
            taskes = len(data)
            with open('{}.csv'.format(argv[1]), mode='w') as record:
                record = csv.writer(record, delimiter=',', quotechar='"',
                                    quoting=csv.QUOTE_ALL)
                for dic in range(0, taskes):
                    record.writerow([argv[1], userName, data[dic].
                                    get('completed'), data[dic].
                                    get('title')])
