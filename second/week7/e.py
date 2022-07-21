#!/usr/bin/env python

import re
import operator

def error_search(log_file):
    users = ''
    errors = 'Timeout while retrieving information|The ticket was modified while updating|Connection to DB failed|Tried to add information to closed ticket|Permission denied while closing ticket|Ticket doesn\'t exist'
    returned_error = []
    per_user= []
    with open(log_file, mode='r',encoding='UTF-8') as file:
        for log in  file.readlines():
            returned_error.extend(re.findall(r"{}".format(errors), log.strip()))
            per_user.extend(re.findall(r""))
        file.close()
    return returned_error

def log_error(returned_error):
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
    
    result = log_error(returned_errors)
    a = sorted(result.items(), key = operator.itemgetter(1), reverse=True)
    print(a)

