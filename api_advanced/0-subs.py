import requests

def number_of_subscribers(subreddit):
    # Reddit API endpoint for getting subreddit information
    api_url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'CustomUserAgent'}

    # Make the request to the Reddit API
    response = requests.get(api_url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        subreddit_info = response.json()

        # Extract and return the number of subscribers
        return subreddit_info['data']['subscribers']
    elif response.status_code == 404:
        # If the subreddit is not found, return 0
        return 0
    else:
        # If there is an error, print the error message and return 0
        print(f"Error: {response.status_code}, {response.text}")
        return 0

# Example usage
subreddit_name = 'python'  # Change this to the subreddit you're interested in
subscribers_count = number_of_subscribers(subreddit_name)

print(f"The number of subscribers in r/{subreddit_name}: {subscribers_count}")
