#!/usr/bin/env python

import re
import operator

def read_file(file):
    per_user = []
    error = []
    err_user = []
    with open(file) as f:
        e = "ERROR"
        i = "INFO"
        for line in f:
            if re.search(r"{}.*".format(i), line.strip()):
                us = (re.search(r"\((.*)\)", line))
                per_user.append(us.group(1))
            if re.search(r"{}.*".format(e), line.strip()):
                erus = (re.search(r"\((.*)\)", line))
                err_user.append(erus.group(1))
            if re.search(r"{}.*".format(e), line.strip()):
                er = re.search(r"ERROR\s(.*)\s\(", line.strip())
                error.append(er.group(1))
        f.close()
    return (per_user, error, err_user)


def arrange_data(per_user, error, err_user):
    user_dic = {}
    error_dic = {}

    # for user in per_user:
    #     if user in user_dic.keys():
    #         user_dic[user] = user_dic[user] + 1
    #     else:
    #         user_dic[user] = 1

    temp_user = []
    for user in per_user:
        if user in user_dic.keys():
            user_dic[user] = []
        else:
            user_dic[user] = 1
        temp_user.append({ n: n, "info": per_user.count(n)})
    new_user =[i for n, i in enumerate(temp_user) if i not in temp_user[n + 1:]]

    for i in new_user:
        for key in i.copy():
            i["error"] = err_user.count(i[key]) 

    for err in error:
        if err in error_dic.keys():
            error_dic[err] = error_dic[err] + 1
        else:
            error_dic[err] = 1
    

    return (new_user, error_dic)

if __name__ == "__main__":
    file = "sys.log"
    (per_user, error, err_user) = read_file(file)
    (ur, er) = arrange_data(per_user, error, err_user)

    # print(per_user)
    # print("======") 
    # print(error)
    # print("======") 
    # print("======") 
    # print(err_user)
    # if(ur.keys())
    # a = sorted(ur.items(), key = operator.itemgetter(0))
    for i in ur:
        print(sorted(i.items(), key = operator.itemgetter(0)))

    # b = sorted(er.items(), key = operator.itemgetter(1))
    # print(a)
    # print(b)