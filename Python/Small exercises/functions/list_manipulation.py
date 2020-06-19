'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

def list_manipulation(list_item, command, location, value=None):
    if command == "remove":
        if location == "end":
            return list_item.pop(-1)  
        elif location == "beginning":
            return list_item.pop(0)
    elif command == "add":
        if location == "beginning":
            list_item.insert(0, value)
            return list_item
        elif location == "end":
            list_item.append(value)
            return list_item
    

    