#!/usr/bin/python3
""" queries the Reddit API and returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    headers = {
        "User-Agent": "0x16-api_advanced",
        "X-Forwared-For": "hossam"
    }
    response = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit), headers=headers).json()
    subs = response.get("data", {}).get("subscribers", 0)
    return subs
