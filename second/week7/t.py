per_user = ['a', 'b', 'c', 'd', 'a']
per_user = ['a', 'b', 'c', 'c', 'c', 'e','e']
temp = []
for n in per_user:
    temp.append({"info": per_user.count(n), "username": n})
new_user =[i for n, i in enumerate(temp) if i not in temp[n + 1:]]


for i in new_user:
    for key in i.copy():
        i["error"] = err_user.count(i[key])
        
print (new_user)
    
    
