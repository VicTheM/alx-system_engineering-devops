#!/usr/bin/python3
"""
This script houses a function that recursively
queries the Reddit api for hot aricles
"""

import requests


def count_words(subreddit, word_list=[]):
    """
    This function counts the number of times each
    word in @word_list appears in the title of
    each hot article on Reddit under a given subreddit
    """
    if word_list:
        word_list = [word.lower() for word in word_list]
    words = {}
    hot_articles = recurse(subreddit)
    for word in word_list:
        n = 0
        for article in hot_articles:
            n += hot_articles.count(word)
        if n > 0:
            words[word] = n
    
    for key, values in words:
        print("{}: {}".format(key, value))


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
