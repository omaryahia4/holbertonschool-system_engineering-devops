#!/usr/bin/python3
"""Reddit API"""

import requests


def top_ten(subreddit):
    """function that queries the Reddit API and returns the
    number of subscriber for a given subreddit"""
    url = "https://www.reddit.com/r/{}/top.json"
    response = requests.get(
        url.format(subreddit), params={"limit": 10})
    res = response.json()

    try:
        for item in res["data"]["children"]:
            print(item["data"]["title"])
    except KeyError:
        print("None")
