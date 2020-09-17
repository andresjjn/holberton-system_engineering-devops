#!/usr/bin/python3
"""This file contain the function number_of_subscribers"""
import requests
import json


def number_of_subscribers(subreddit):
    """Funtion that return the number of subscribers of a subreddit"""
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    request = requests.get(url, headers=headers, allow_redirects=False)
    
    if request.status_code == 200:
        return json.loads(request.text)['data']['subscribers']
    return 0
