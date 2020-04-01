def my_binary_search(my_list, item_search):
 found=(-1,-1)
 low = 0
 high = len(my_list) - 1
 while low <= high:
 mid = (low + high) // 2
 if my_list[mid] == item_search:
 return my_list[mid],mid
 elif my_list[mid] > item_search:
 high = mid - 1
 else:
 low = mid + 1
 return found # None
