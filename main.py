# Reverse - reverses a list
# params: list of numbers
# return: reversed list
def reverse(list):
    return list[::-1]

# Find Max - finds the max number in list
# params: list of numbers
# return: max number
def find_max(list):
    if len(list) > 0:
        max = list[0]
        for i in range(len(list)):
            if i > max:
                max = i
        return max
    else:
        return 'List is empty.'

# Find Min: find the minimum number in the list
# params: list of numbers
# return: min number in list
def find_min(list):
    if len(list) > 0:
        min = list[0]
        for i in range(len(list)):
            if i < min:
                min = i
        return min
    else:
        return 'List is empty.'

#Find Difference Between 2 Lists
#params: 2 lists
#return: list of unqiue elements
def find_diff(list1, list2):
    unique_items = list(set(list1) - set(list2))
    unique_items += list(set(list2) - set(list1))
    return unique_items

def find_subset(list, sublist):
    if not list:
        print('List is empty')
        return
    if not sublist:
        print('Sub List is empty')
        return
    for i in range(len(list)):
        if list[i] == sublist[0]:
            for y in range(len(sublist)):
                if list[i+y] == sublist[y]:
                    continue
                else:


def rotate(list):
    pass

# Linear Sorting - sorts a list by ascending or descending order
# params: list of numbers, boolean ascend
# return: sorted list
def linear_sort(list, ascend):
    list_len = len(list)
    for i in range(list_len):
        for j in range(i+1, list_len):
            if ascend:
                if list[i] > list[j]:
                    list[i], list[j] = list[j], list[i]
            else:
                if list[i] < list[j]:
                    list[i], list[j] = list[j], list[i]
    return list

# Linear Search - searches for a target value sequentially through list
# params: list to be searched, value to be found
# return: True if target value found, False otherwise
def linear_search(list, target):
    for i in range(len(list)):
         if list[i] == target:
             return True
    return False

# Bubble Sort -
# params:
# returns:
def bubblesort(list):
    ll = len(list)
    for i in range(ll - 1):
        for j in range(ll-i-1):
            if list[j] > list[i]:
                list[j], list[i] = list[i], list[j]
                print(list)
    print(list)
    return



arr = [2, 4, 9, 2, 93, 89, 49, 90, 55, 66, 77, 44, 33, 2233, 234543, 223, 2, 6]

arr1 = [ 2, 3, 4, 5]
arr2 = [4, 5, 6, 7]
target = 33
other_target = 4908


list1 = [-10, 21, -4, -45, -66, 93]
list2 = []

#Difference Between Two Lists
#print(find_diff(arr1, arr2))

find_subset(list2, list1)