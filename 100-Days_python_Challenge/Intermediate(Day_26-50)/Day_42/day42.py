# Day 42: Working with APIs and JSON Data
# This script demonstrates fetching data from a web API and parsing JSON responses.
# We use the 'requests' library for HTTP requests and Python's built-in 'json' module for parsing.
# Example API: JSONPlaceholder (https://jsonplaceholder.typicode.com/) - free fake data, no API key needed.

import requests  # For making HTTP requests to APIs
import json      # For parsing JSON data (though requests can handle it directly)

# Base URL for the example API
base_url = "https://jsonplaceholder.typicode.com"

# Example 1: Fetching JSON data from an API endpoint
# We'll get a list of posts. This sends a GET request to the API.
response = requests.get(f"{base_url}/posts")  # f-string for URL building
if response.status_code == 200:  # 200 means success
    print("Example 1 - Raw JSON Response (first 500 chars):")
    print(response.text[:500] + "...")  # Print a snippet of the raw JSON text
else:
    print("Example 1 - Failed to fetch data. Status code:", response.status_code)

# Example 2: Parsing JSON into Python objects
# response.json() automatically converts JSON to a Python list of dictionaries.
if response.status_code == 200:
    posts = response.json()  # Parse JSON
    print("\nExample 2 - Parsed Data Type:", type(posts))  # Should be <class 'list'>
    print("First post (as dict):", posts[0])  # Access the first item
else:
    posts = []  # Empty list if failed

# Example 3: Extracting specific data from the parsed JSON
# Loop through posts and pull out titles and user IDs.
if posts:
    print("\nExample 3 - Extracted Titles and User IDs:")
    for post in posts[:5]:  # Show first 5 for brevity
        title = post.get("title", "No title")  # Use .get() to avoid errors
        user_id = post.get("userId", "Unknown")
        print(f"User {user_id}: {title}")
else:
    print("Example 3 - No data to extract.")

# Example 4: Fetching data for a specific item (e.g., a single user)
# Get details for user ID 1.
user_response = requests.get(f"{base_url}/users/1")
if user_response.status_code == 200:
    user = user_response.json()  # Parse JSON
    print("\nExample 4 - User Details:")
    print(f"Name: {user.get('name')}")
    print(f"Email: {user.get('email')}")
    print(f"City: {user.get('address', {}).get('city', 'Unknown')}")  # Nested dict access
else:
    print("Example 4 - Failed to fetch user. Status code:", user_response.status_code)

# Example 5: Handling errors and checking response details
# Try fetching from a non-existent endpoint to simulate an error.
error_response = requests.get(f"{base_url}/nonexistent")
print("\nExample 5 - Error Handling:")
print("Status Code:", error_response.status_code)  # Likely 404 (Not Found)
if error_response.status_code != 200:
    print("Error: Could not fetch data. Check the URL or try again later.")
else:
    print("Data fetched successfully.")

# Bonus: Saving JSON data to a file for later use
if posts:
    with open("posts.json", "w") as file:
        json.dump(posts, file, indent=4)  # Save parsed data as formatted JSON
    print("\nBonus - Saved posts to 'posts.json'. Check your folder!")

# Experiment: Change the endpoint (e.g., /comments or /todos) and run again!
# Note: Always respect API rate limits and terms of service.
