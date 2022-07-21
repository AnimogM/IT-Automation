#!/usr/bin/env python

import re
import csv
import operator

def get_data(filename):
    """read the file and return data"""
    per_user = []
    user = {}
    info = {}
    error = {}

    with open(filename) as file:
        for line in file:
            #check for user info and error
            if re.search(r"INFO.*", line.strip()):
                er_user = re.search(r"\((.*)\)", line)
                info[er_user.group(1)] = info.get(er_user.group(1), 0) + 1
            #check for error and count and add to error
            if re.search(r"ERROR.*", line.strip()):
                er_user = re.search(r"\((.*)\)", line)
                er = re.search(r"ERROR\s(.*)\s\(", line.strip())
                error[er.group(1)] = error.get(er.group(1), 0) + 1
                user[er_user.group(1)] = user.get(er_user.group(1), 0) + 1

    for key, value in user.items():
        per_user.append({"Username": key, "INFO": info.get(key, 0), "ERROR": value})

    return (error, per_user)


def sort_data(error, user):
    """sort error list in descending order and user list by name"""

    errors = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
    users = sorted(user, key=lambda i: i['Username'])
    return (errors, users)

def write_to_csv(errors, users):
    """write to csv file"""

    field_err = ["Error", "Count"]
    field_user = ["Username", "INFO", "ERROR"]

    with open("error_message.csv", "w", newline="") as er_csv:
        writer = csv.writer(er_csv)
        writer.writerow(field_err)
        for row in errors[:8]:
            writer.writerow(row)
    with open("user_statistics.csv", "w", newline="") as user_csv:
        writer = csv.DictWriter(user_csv, fieldnames=field_user)
        writer.writeheader()
        writer.writerows(users[:8])

if __name__ == "__main__":
    (error, per_user) = get_data("syslog.log")
    (errors, users) = sort_data(error, per_user)
    write_to_csv(errors, users)
