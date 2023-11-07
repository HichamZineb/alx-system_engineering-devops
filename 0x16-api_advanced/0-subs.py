#!/usr/bin/python3
""" 0. How many subs? """


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number
    of total subscribers for a given subreddit
    """
    import requests

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "UserAgent"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    return response.json().get("data").get("subscribers")
