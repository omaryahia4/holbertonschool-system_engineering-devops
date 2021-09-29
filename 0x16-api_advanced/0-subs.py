#!/usr/bin/python3
"""Reddit API"""

import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and returns the
    number of subscriber for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json"
    response = requests.get(
        url.format(subreddit))
    res = response.json()
    try:
        return res['data']["subscribers"]
    except KeyError:
        return 0
