#!/usr/bin/python3
"""Fisrt question with APIs"""

import requests
import sys


def main():
    """main function"""
    user_id = int(sys.argv[1])

    todo_url = 'https://jsonplaceholder.typicode.com/todos'

    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    todo_res = requests.get(todo_url)

    number_of_task = 0

    completed_tasks = []

    for todo in todo_res.json():
        if todo['userId'] == user_id:
            number_of_task += 1

            if todo['completed']:
                completed_tasks.append(todo['title'])

    user_name = requests.get(user_url).json()['name']

    output = "Employee {} is done with tasks({}/{}):"\
        .format(user_name, len(completed_tasks), number_of_task)

    print(output)

    for task_title in completed_tasks:
        print("\t {}".format(task_title))


if __name__ == "__main__":
    main()
