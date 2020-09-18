#!/usr/bin/python3
"""This file contain the function recurse"""
import requests


def recurse(subreddit, hot_list=[], aftervalue="aftervalue"):
    """Recursive funtion that return the top ten of a subreddit"""
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

    if aftervalue == "aftervalue":
        url = "https://www.reddit.com/r/" + subreddit + "/hot/.json"
    else:
        url = "https://www.reddit.com/r/" + subreddit + "/hot/.json?after=" \
            + aftervalue
    request = requests.get(url, headers=header, allow_redirects=False)
    if request.status_code != 200:
        return None

    data = request.json().get("data")
    after = request.json().get("data").get("after")
    children = data.get("children")
    for i in children:
        titles = i.get("data").get("title")
        hot_list.append(titles)
    if after:
        return (recurse(subreddit, hot_list, after))
    return(hot_list)
