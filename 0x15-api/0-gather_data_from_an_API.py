#!/usr/bin/python3
"""
This script returns an employee's to-do list progress using a REST API.
"""

import requests
import sys


def get_employee_task_status(employee_id):
    """
    Gets and displays the TODO list progress for a given employee ID.
    """
    main_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{main_url}/users/{employee_id}"
    todos_url = f"{main_url}/todos?userId={employee_id}"

    try:
        # Get employee information
        user_info = requests.get(user_url)
        user_data = user_info.json()
        EMPLOYEE_NAME = user_data.get("name")

        # Get TODO list for the employee
        todos_response = requests.get(todos_url)
        todos_list = todos_response.json()

        # Determine progress
        TOTAL_NUMBER_OF_TASKS = len(todos_list)
        NUMBER_OF_DONE_TASKS = sum(
            1 for todo in todos_list
            if todo.get("completed")
            )

        # Display progress
        print(f"Employee {EMPLOYEE_NAME} is done with tasks"
              f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")

        # Display completed tasks
        for todo in todos_list:
            if todo.get("completed"):
                TASK_TITLE = todo.get('title')
                print(f"\t {TASK_TITLE}")

    except requests.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_task_status(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)
