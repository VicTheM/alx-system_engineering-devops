#!/usr/bin/python3
"""This module houses a function that returns the number
of suscribers to a subreddit using the reddit api."""


import requests


def number_of_subscribers(subreddit):
    """This function returns the number of
    subscribers to subreddit on the reddit
    site."""

    header = {
            'User-Agent': 'VictoryBot'
            }

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code == 200:
        subscribers = (response.json())["data"]["subscribers"]
        return subscribers

    return 0
