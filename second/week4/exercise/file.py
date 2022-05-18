#!/usr/bin/env python3

import sys
import os
import re


def error_search(log_file):
    error = input("What is the error? ")
    returned_error = []
    with open(log_file, mode='r',encoding='UTF-8') as file:
        for log in  file.readlines():
            error_patterns = ["error"]
            for i in range(len(error.split(' '))):
                error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
            if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                returned_error.append(log)
        file.close()
    return returned_error

def file_output(returned_error):
    with open('errors_found.log', 'w') as file:
        for error in returned_error:
            file.write(error)
        file.close()

if __name__ == "__main__":
    log_file = sys.argv[1]
    print("this is it, ", sys.argv[1])
    returned_errors = error_search(log_file)
    # print(returned_errors)
    file_output(returned_errors)
    sys.exit(0)
