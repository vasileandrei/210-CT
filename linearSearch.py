def linearSearch(myList, myItem):

    found = False
    position = 0

    while position < len(myList) and not found:
        if myList[position] == myItem:
            found = True
        position = position + 1

    if found == True:
        print ("Item found")
    else:
        print ("Item not found")
