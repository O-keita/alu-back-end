#!/usr/bin/python3
"""Export results from the API as CSV"""

import csv
import requests
import sys


def main():
    """Main function"""
    user_id = int(sys.argv[1])

    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    try:
        user_name = requests.get(user_url).json()['username']
    except requests.RequestException as e:
        print("Error fetching user details:", e)
        sys.exit(1)

    try:
        todo_data = requests.get(todo_url)
        todo_data.raise_for_status()  # Raise an HTTPError for bad responses
        todo_data = todo_data.json()
    except requests.RequestException as e:
        print("Error fetching todos:", e)
        sys.exit(1)

    data_file = []

    for todo in todo_data:
        if todo['userId'] == user_id:
            data_file.append([
                str(user_id),
                user_name,
                todo['completed'],
                todo['title']
            ])

    file_name = "{}.csv".format(user_id)

    with open(file_name, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for row in data_file:
            writer.writerow(row)

    print("Exported completed tasks to {}".format(file_name))

if __name__ == '__main__':
    main()
