#!/usr/bin/python3
"""Export results from the API as CSV"""

import requests
import sys
import csv

def main():
    """main function"""
    user_id = int(sys.argv[1])

    todo_url ='https://jsonplaceholder.typicode.com/todos'
    user_url ='https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    user_name = requests.get(user_url).json()['name']

    todo_data = requests.get(todo_url)

    data_file =[] 

    for todo in todo_data.json():
        if todo['userId'] == user_id:
            data_file.append(
                [
                    str(user_id),
                    user_name,
                    todo['completed'],
                    todo['title']
                    
                ]
            )
    
    file_name = "{}.csv".format(user_id)

    with open(file_name, 'w', newline='') as csv_file:

        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for row in data_file:
            for item in row:
                str(item)
                print(item)
                writer.writerow(row)



if __name__ == '__main__':
    main()


