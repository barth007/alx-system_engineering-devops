#!/usr/bin/python3
"""
   returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        subcribers_data = data["data"]
        subcribers = subcribers_data["subscribers"]
        return subcribers
