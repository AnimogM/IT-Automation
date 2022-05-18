#!/usr/bin/env python

import csv
import re


def save_file(file):
    """open a file and returns the content of the file"""
    content_list = []
    field = set()
    try:
        with open(file) as f:
            reader = csv.DictReader(f)

            for row in reader:
                content_list.append([values.strip() for values in row.values()])
                field.update([keys.strip() for keys in row.keys()])
        return (content_list, field)
    except FileNotFoundError as e:
        return e

def check_pattern(lists):
    """checks the list of emails"""
    pattern = r"(@abc.edu)"
    newlist = []

    for item in lists:
        if re.search(pattern, item[1]):
            item[1] = re.sub(pattern,"@maryam.com", item[1])         
        newlist.append({"Full Name": item[0], "Email Address": item[1]})
    return newlist


content_lists, newfield = save_file("file.csv")
result = check_pattern(content_lists)

with open("result.csv", 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=newfield, delimiter=',')
    writer.writeheader()

    writer.writerows(result)
