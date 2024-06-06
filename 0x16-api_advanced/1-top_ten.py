"""This script queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit."""

import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a given subreddit.
    If an invalid subreddit is given, prints None."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "VictoryBot"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)