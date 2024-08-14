#!/usr/bin/python3
"""This script houses a function that recursively queries the Reddit API and
returns a list containing the titles of all hot articles for a given subreddit."""

import requests

def recurse(subreddit, hot_list=[]):
    """Recursively returns all hot artical for
    a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?".format(subreddit)
    headers = {"User-Agent": "VictoryBot"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])

        after = data['data'].get('after', None)
        if after is not None:
            recurse(subreddit, hot_list)

    if not hot_list:
        return None
    
    return hot_list


print(len(recurse("programming")))
