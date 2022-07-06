# from math import ceil, floor
# ar = [3,2,5,6,9,1,7]
# ar.sort()
# min_val = 0
# max_val = len(ar)-1
# val = int(input("Enter you value: "))

# while min_val < max_val:
#     mid_val = (min_val+max_val)//2
#     if ar[mid_val] == val:
#         print("Search found at index %d" %mid_val)
#         break
#     elif ar[mid_val]> val:
#         max_val = mid_val - 1
#     else:
#         min_val = mid_val + 1

# if min_val==max_val:
#     print("Search not found")

def binary_search(l, target, low = None, ri = None):
    if low is None:
        low = 0
    if ri is None:
        ri = len(l)-1
    if low > ri:
        return -1

    mid = (low+ri)//2
    if l[mid]==target:
        return mid
    elif l[mid]<target:
        return binary_search(l, target, mid+1, ri)
    else:
        return binary_search(l, target, low, mid-1)


if __name__ =='__main__':
    l = [1,2,3,4,5]
    target = 1
    print(binary_search(l,target))

