!/usr/bin/python3

"""Exports to-do list information for a given employee ID to CSV format."""

import csv
import requests
import sys


user_id = sys.argv[1]
url = "https://jsonplaceholder.typicode.com/"
user = requests.get(url + "users/{}".format(user_id)).json()
username = user.get("username")
params = {"userId": user_id}
todos = requests.get(url + "todos", params).json()
export[user_id] = [
        {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": user.get("username"),
        }
        for todo in todo_list
    ]

return export
if __name__ == "__main__":
    data_to_export = fetch_user_data()
with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data_to_export, jsonfile, indent=4)

