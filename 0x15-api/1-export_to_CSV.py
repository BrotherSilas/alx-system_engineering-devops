#!/usr/bin/python3
"""
This script gets TODO list information for a given employee ID
using a REST API and exports it to a CSV file.
"""

import csv
import requests
import sys


def get_employee_task_status(user_id):
    """
    Gets TODO list information for a given employee ID and exports it to a CSV file.
    """
    main_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{main_url}/users/{user_id}"
    todos_url = f"{main_url}/todos?userId={user_id}"

    try:
        # Get employee information
        user_info = requests.get(user_url)
        user_data = user_info.json()
        username = user_data.get("username")

        # Get TODO list for the employee
        todos_response = requests.get(todos_url)
        todos_list = todos_response.json()

        # Prepare CSV file name
        csv_filename = f"{user_id}.csv"

        # Write data to CSV file
        with open(csv_filename, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            for todo in todos_list:
                csv_writer.writerow([
                    user_id,
                    username,
                    str(todo.get("completed")),
                    todo.get("title")
                ])

        print(f"Data exported to {csv_filename}")

    except requests.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <user_id>")
        sys.exit(1)

    try:
        user_id = int(sys.argv[1])
        get_employee_task_status(user_id)
    except ValueError:
        print("Error: USER ID must be an integer")
        sys.exit(1)
