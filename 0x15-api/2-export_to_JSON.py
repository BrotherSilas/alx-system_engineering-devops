#!/usr/bin/python3
"""
This script retrieves TODO list data for a given employee ID
using a REST API and exports it to a JSON file.
"""

import json
import requests
import sys


def get_employee_todo_data(employee_id):
    """
    Gets TODO list data for a given employee ID and exports it to a JSON file.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Get employee information
        user_response = requests.get(user_url)
        user_data = user_response.json()
        username = user_data.get("username")

        # Get TODO list for the employee
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Prepare JSON data
        json_data = {str(employee_id): []}
        for todo in todos_data:
            json_data[str(employee_id)].append({
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
            })

        # Write data to JSON file
        json_filename = f"{employee_id}.json"
        with open(json_filename, 'w') as json_file:
            json.dump(json_data, json_file)

        print(f"Data exported to {json_filename}")

    except requests.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_data(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)
