a_list = [10,12,14,14,16,28,28,30]
new_list=[]

def removeDuplicates(list,new):
    for item in list:
        if item not in new:
            new.append(item)

removeDuplicates(a_list,new_list)

print("The first list is:",a_list)
print("The new list is:",new_list)

def sortList(list):
    list.sort(reverse=True)

sortList(new_list)
print("New list in descending order is:",new_list)
