'''
Write a Python program to calculate the length of a string.
Write a Python program to get the largest number from a list
. Write a Python program to count the number of characters in a string
Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string is already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
5) Find the common elements between two tuples.
tup1 = (1, 2, 3, 4)
tup2 = (3, 4, 5, 6)

6) Create a tuple of immutable objects, then attempt to modify one of the element of the tuple. Explain what would happen

7) Write a python program to concatenate 2 tuples and create a new tuple without using the + operator

8) Write a python program to unpack a tuple into individual variables

9) Write a program to find the difference between two tuples

10) Write a program to convert a list of tuples into list of strings by concatenating elements of each tuple

11) Given a list of integers, write a function that returns the two numbers that sum to zero. If there are multiple pairs that sum to zero, return the pair with the smallest non-negative element. If there are no elements that sum to zero, return an empty list.
For example, given the list [1, 2, 3, -2, -1], the function should return [-2, 2] because -2 + 2 equals 0.

'''


# 1
def calculate_length(s):
    leng = 0
    for char in s:
        leng += 1
    return leng


# 2
def largest_number(li):
    maximum = li[0]
    for i in li:
        if i > maximum:
            maximum = i
    return maximum


# 3
def calculate_frequency(s):
    dicti = {}
    for char in s:
        if char in dicti:
            dicti[char] += 1
        else:
            dicti[char] = 1
    return dicti


# 4


# 5
def similar_element(t1, t2):
    l1 = []
    for ele in t1:
        if ele in t2:
            l1.append(ele)
    return l1


# 6
def check(t1):
    t1[1] = 4
    return t1

#7
def add(t1,t2):
    l1=list(t1)
    l2=list(t2)
    l1.extend(l2)
    t3=tuple(l1)
    return t3

#8
def unpack(t1):
    t2=t1[0:3]
    t3=t1[3:]
    print(t2)
    print(t3)

#9
def diff(t1,t2):
        l1 = []
        for ele in t1:
            if ele not in t2:
                l1.append(ele)
        for ele in t2:
            if ele not in t1:
                l1.append(ele)

        return l1
#10
def convertt(lst):
    res=[]
    for tup in lst:
        s = ""
        for ele in tup:
            s+=str(ele)
        res.append(s)
    return (res)

#############################################################################################

l = calculate_length("abcd")
print(l)

maxi = largest_number([1, 2, 6, 3])
print(maxi)

freq = calculate_frequency("aabgfdsaddcde")
print(freq)

tup1 = (1, 2, 3, 4, "aa")
tup2 = (3, 4, 5, 6, "aa", "bb")

similar = similar_element(tup1, tup2)
print(similar)

# t = check(tup1)
# print(t)

add(tup1,tup2)

unpack(tup1)

t=diff(tup1,tup2)
print(t)

lst=[(1,2,3),(1,2,3),(1,2,3)]
res=convertt(lst)
print(res)

