#!/usr/bin/python3
""" 3. Count it! """

import requests


def count_words(subreddit, word_list, after=None, wc={}):
    """
    Queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.
    """

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "UserAgent"}
    params = {"after": after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json().get("data")
    children = data.get("children")
    after = data.get("after")

    for child in children:
        title = child.get("data").get("title").lower()
        for word in word_list:
            if " {} ".format(word.lower()) in " {} ".format(title):
                wc[word.lower()] = wc.get(word.lower(), 0) + 1

    if after:
        return count_words(subreddit, word_list, after, wc)
    else:
        sorted_word_counts = sorted(wc.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_word_counts:
            print("{}: {}".format(word, count))
