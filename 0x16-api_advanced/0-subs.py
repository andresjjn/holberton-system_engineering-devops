#!/usr/bin/python3
"""This file contain the function number_of_subscribers"""
import requests
import json


def number_of_subscribers(subreddit):
    """Funtion that return the number of subscribers of a subreddit"""
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
                            AppleWebKit/537.36 (KHTML, like Gecko)\
                            Chrome/70.0.3538.77 Safari/537.36"
                    }
    url = 'https://www.reddit.com/' + '/r/' + subreddit + '/about.json'
    request = json.loads(requests.get(url,
                         headers=headers, allow_redirects=False).text)
    result = request.get('data', {}).get('subscribers')
    if result is None:
        return 0
    return result

if __name__ == "__main__":
    number_of_subscribers('programming')
