#!/usr/bin/python3
""" Script to query a list of all hot posts on a given Reddit subreddit."""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Recursively retrieves a list of titles of all hot posts
    on a given subreddit"""

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "LearApi/0.0.1"}
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    # Send a GET request to the subreddit's hot posts page
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Check if the response status code indicates a not-found error (404)
    if response.status_code == 404:
        return None
    # Parse the JSON response and extract relevant data
    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    # Append post titles to the hot_list
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    # If there are more posts to retrieve, recursively call the function
    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    # Return the final list of hot post titles
    return hot_list
