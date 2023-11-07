#!/usr/bin/python3
""" 1. Top Ten """


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit.
    """
    import requests

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "UserAgent"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return 0

    try:
        data = response.json().get("data").get("children")
        for post in data:
            print(post.get("data").get("title"))
    except Exception as e:
        print(None)
