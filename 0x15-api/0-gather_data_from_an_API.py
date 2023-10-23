#!/usr/bin/python3

"""
Script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

from requests import get
import sys


def fetch_todo_list(employee_id):
    """
    Returns employee TODO list progress from API and displays the information.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    user_response = get(user_url)
    todos_response = get(todos_url)

    user_data = user_response.json()
    todos_data = todos_response.json()

    done_tasks = [task['title'] for task in todos_data if task['completed']]
    all_t = len(todos_data)
    dt_l = len(done_tasks)

    print(f"Employee {user_data['name']} is done with tasks({dt_l}/{all_t}):")
    for task in done_tasks:
        print(f"\t{task}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        fetch_todo_list(employee_id)
