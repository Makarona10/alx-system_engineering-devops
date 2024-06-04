#!/usr/bin/python3
"""API to query the Reddit API and returns the number
of subscribers for a given subreddit"""


import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers"""
    res = requests.get("https://www.reddit.com/r/{}/about.json".format(subreddit),
                       headers={"User-Agent": "Python/requests"})
    if not res or res.status_code == 404:
        return 0
    data = res.json().get("data").get("subscribers")
    if data:
        return data
    else:
        return 0
