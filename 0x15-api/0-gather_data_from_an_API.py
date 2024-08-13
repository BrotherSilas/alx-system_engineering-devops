#!/usr/bin/python3
"""
This script gets information about an employee's to-do list using a REST API and displays the progress status.
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
        employee_name = user_data.get("name")

        # Get TODO list for the employee
        todos_response = requests.get(todos_url)
        todos_list = todos_response.json()

        # Determine progress
        total_number_of_tasks = len(todos_list)
        number_of_done_tasks = sum(1 for todo in todos_list if todo.get("completed"))

        # Display progress
        print(f"Employee {employee_name} is done with tasks"
              f"({number_of_done_tasks}/{total_number_of_tasks}):")

        # Display completed tasks
        for todo in todos_list:
            if todo.get("completed"):
                print(f"\t {todo.get('title')}")

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
