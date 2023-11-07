#!/usr/bin/python3
""" 2. Recurse it! """

import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """
    Queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "UserAgent"}
    params = {"after": after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data")
    children = data.get("children")
    after = data.get("after")
    count = data.get("count")

    hot_list += [child.get("data").get("title") for child in children]

    if not after:
        return hot_list

    return recurse(subreddit, hot_list, count, after)
