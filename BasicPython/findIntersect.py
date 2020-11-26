lists = ["12, 3, 4, 77, 9", "1, 12, 77, 3, 5"]
set1 = set(lists[0].split(", "))
set2 = set(lists[1].split(", "))
set3 = set1 & set2
print(sorted(set3,key=int))
                           
