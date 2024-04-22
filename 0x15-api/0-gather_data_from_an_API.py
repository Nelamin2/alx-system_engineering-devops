#!/usr/bin/python3

"""Returns to-do list to a given employee"""

import requests
import sys

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    emp_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(employee_id)).json()
    Parameters = {"userId": employee_id}
    todos = requests.get(url + "todos", params).json()
    completed = [i.get("title") for i in todos if i.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(complete)) for complete in completed]
