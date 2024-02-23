#!/usr/bin/python3
"""Export Everything to JSON"""

import json
import requests


def main():
    """Main function"""

    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = 'https://jsonplaceholder.typicode.com/users'

    # Fetch user data
    user_data = requests.get(user_url).json()

    response = requests.get(todo_url)
    output = {}

    for todo in response.json():
        user_id = todo.get('userId')

        if user_id not in output.keys():
            # Fetch the username for the specific user
            username = next((user['username'] for user in user_data
                            if user['id'] == user_id), None)
            output[user_id] = []

        output[user_id].append({
            "username": username,
            "task": todo.get('title'),
            "completed": todo.get('completed')
        })

    # Write to JSON file outside the loop
    with open("todo_all_employees.json", 'w', newline="") as json_file:
        json.dump(output, json_file, indent=2)


if __name__ == "__main__":
    main()
