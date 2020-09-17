#!/usr/bin/python3
"""This file contain the function top_ten"""
import requests


def top_ten(subreddit):
    """Funtion that return the top ten of a subreddit"""
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json?limit=10'
    request = requests.get(url, headers=headers, allow_redirects=False)

    if request.status_code == 200:
        dic = request.json()['data']['children']
        for i in range(0, 10):
            print(dic[i]['data']['title'])
    else:
        print("None")

if __name__ == "__main__":
    top_ten('programing')
