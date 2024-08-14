#!/usr/bin/python3
"""
Module for counting occurrences of keywords in article titles of a subreddit.
"""
import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries the Reddit API, parses the titles of hot articles,
    and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): A list of keywords to count.
        after (str): A token for pagination (default is None).
        word_count (dict): A dictionary to store word counts (default is {}).

    Returns:
        None
    """
    # Set up the API request
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100, "after": after}

    # Send the request
    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

    # Check if the subreddit is valid
    if response.status_code != 200:
        return

    # Parse the response
    data = response.json()["data"]

    # Process the titles
    for post in data["children"]:
        title = post["data"]["title"].lower()
        for word in word_list:
            word = word.lower()
            # Count exact word matches
            count = title.split().count(word)
            if count > 0:
                if word in word_count:
                    word_count[word] += count
                else:
                    word_count[word] = count

    # Check if there are more pages
    if data["after"]:
        # Recursive call with the new 'after' token
        return count_words(subreddit, word_list, data["after"], word_count)
    else:
        # Print the results
        sorted_counts = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print(
             "Ex: {} programming 'python java javascript'".format(sys.argv[0])
                )
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
