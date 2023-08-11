#!/usr/bin/python3
"""
   return list containing the titles of all hot articles
"""
import requests
import json


def recurse(subreddit, hot_list=[], after=None):
    params = {
              "limit": 100,
              "after": after
            }
    headers = {
               "User-Agent": "Custom"
            }
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"

    response = requests.get(
                           url, headers=headers,
                           params=params, allow_redirects=False
                        )
    if response.status_code == 200:
        data = json.loads(response.content)
        hot_articles = data["data"]["children"]

        for article in hot_articles:
            hot_list.append(article["data"]["title"])

        after = data["data"]["after"]

        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
