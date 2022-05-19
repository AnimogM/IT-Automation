#!/usr/bin/env python

import sys
import re

def error_search(log_file):
    errors = 'Timeout while retrieving information|The ticket was modified while updating|Connection to DB failed|Tried to add information to closed ticket|Permission denied while closing ticket|Ticket doesn\'t exist'
    returned_error = []
    with open(log_file, mode='r',encoding='UTF-8') as file:
        for log in  file.readlines():
            returned_error.extend(re.findall(r"{}".format(errors), log.strip()))
        file.close()
    return returned_error

def file_output(returned_error):
    dic = {}
    for error in returned_error:
        if error in dic.keys():
            dic[error] = dic[error] + 1
        else:
            dic[error] = 1
    return dic

if __name__ == "__main__":
    log_file = "sys.log"
    returned_errors = error_search(log_file)
    
    print(file_output(returned_errors))

