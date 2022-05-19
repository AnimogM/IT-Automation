list1 = ['a', 'b', 'c', 'd', 'a']
list2 = ['a', 'b', 'c', 'c', 'c', 'e','e']
d = []
for n in list2:
    d.append({"no": list2.count(n), "name": n})
nn =[i for n, i in enumerate(d) if i not in d[n + 1:]]


for i in nn:
    for key in i.copy():
        i["error"] = list1.count(i[key])
        
print (nn)
    
    
