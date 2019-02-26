list.append(x) : equiv to a[len(a): ] = [x] 
list.extend(x)

   I.e. list1.extend(list2)

list.insert(i, x) : insert an item at a given position 
list.remove(x) : remove the first item from the list whose value is x (error if such item DNE)

list.pop([i]) : remove item from given position on list
list.index(x) : return the index of the first item whose value is x 

list.count(x) : return the number of times x appears on the list
list.sort(cmp=None, key=None, reverse=False)

list.reverse() : reverse the elements of the list, in place


