#!/usr/bin/python3
"""
Module for recursively querying the Reddit API and returning hot article titles.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): A list to store the hot article titles (default is []).
        after (str): A token for pagination (default is None).

    Returns:
        list: A list of hot article titles if successful, None otherwise.
    """
    # Set up the API request
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    params = {"limit": 100, "after": after}

    # Send the request
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Check if the subreddit is valid
    if response.status_code != 200:
        return None

    # Parse the response
    data = response.json()["data"]
    
    # Add titles to the hot_list
    for post in data["children"]:
        hot_list.append(post["data"]["title"])

    # Check if there are more pages
    if data["after"]:
        # Recursive call with the new 'after' token
        return recurse(subreddit, hot_list, data["after"])
    else:
        # No more pages, return the complete list
        return hot_list


if __name__ == '__main__':
    print(recurse("programming"))
