#!/usr/bin/python3
"""Export to JSON using dump"""

import json
import requests
import sys


def main():
    """main function"""

    user_id = int(sys.argv[1])
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    user_info = []
    user_file = {user_id: user_info}

    response = requests.get(todo_url).json()
    user_name = requests.get(user_url).json().get('username')

    for todo in response:
        if todo.get('userId') == user_id:
            user_info.append({
                "task": todo.get('title'),
                "completed": todo.get('completed'),
                "name": user_name
            })

    file_name = "{}.json".format(user_id)

    with open(file_name, 'w', newline='') as json_file:
        json.dump(user_file, json_file)


if __name__ == '__main__':
    main()
