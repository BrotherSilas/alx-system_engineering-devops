#!/usr/bin/python3
"""
This script retrieves TODO list data for all employees
using a REST API and exports it to a JSON file.
"""

import json
import requests


def get_all_employees_todo_data():
    """
    Retrieves TODO list data for all employees and exports it to a JSON file.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users"
    todos_url = f"{base_url}/todos"

    try:
        # Get all users
        users_response = requests.get(users_url)
        users_data = users_response.json()

        # Get all todos
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Prepare JSON data
        all_employees_data = {}

        for user in users_data:
            user_id = str(user['id'])
            username = user['username']
            user_todos = [todo for todo in todos_data if todo['userId'] == user['id']]

            all_employees_data[user_id] = [
                {
                    "username": username,
                    "task": todo['title'],
                    "completed": todo['completed']
                }
                for todo in user_todos
            ]

        # Write data to JSON file
        json_filename = "todo_all_employees.json"
        with open(json_filename, 'w') as json_file:
            json.dump(all_employees_data, json_file)

        print(f"Data exported to {json_filename}")

    except requests.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    get_all_employees_todo_data()
