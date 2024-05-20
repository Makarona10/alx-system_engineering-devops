#!/usr/bin/python3
"""Gather data module"""

from sys import argv
import requests
import json


def get_user_tasks():
    emp_id = int(argv[1])
    user = f'https://jsonplaceholder.typicode.com/users/{emp_id}'
    todos = f'{user}/todos'
    todo_list = requests.get(todos).json()
    user = requests.get(user).json()

    done_todo = []

    for todo in todo_list:
        if todo.get('completed') is True:
            done_todo.append(todo.get('title'))

    print("Employee {} is done with tasks({}/{}): "
          .format(user.get('name'), len(done_todo), len(todo_list)))
    for todo in done_todo:
        print("\t {}".format(todo))


if __name__ == '__main__':
    todo_list = get_user_tasks()
