#!/usr/bin/python3
"""
   It fetches the title of top 10 posts and print them
"""
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        children_data = data["data"]
        title_data = children_data["children"]
        for title in title_data:
            title_data = title["data"]["title"]
            print(title_data)
    elif response.status_code == 302:
        print(None)
    else:
        print(None)
