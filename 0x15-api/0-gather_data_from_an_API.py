#!/usr/bin/python3
"""This script retrievs a user task details from a REST API"""

import sys
import requests

if __name__ == "__main__":
    userID = int(sys.argv[1])
    nameURL = "https://jsonplaceholder.typicode.com/users" + "/" + str(userID)
    todoURL = "https://jsonplaceholder.typicode.com/todos"

    res = requests.get(nameURL)
    user = res.json()

    params = {
            "userId": userID
            }
    res = requests.get(todoURL, params=params)
    tasks = res.json()

    completed = 0
    total = len(tasks)
    for task in tasks:
            if (task["completed"] is True):
               completed = completed + 1


    print("Employee {} is done with tasks({}/{}):".format(user["name"], completed, total))
    for task in tasks:
        if task["completed"] is True:
                print("\t {}".format(task["title"]))
