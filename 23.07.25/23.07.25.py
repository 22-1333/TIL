# 1

'''
# count people by blood type

# result => {"A" : 3. "B" : 3, "O" : 3, "AB" : 3}

blood_types = ["A", "B", "A", "O", "AB", "AB", "O", "A", "B", "O", "B", "AB"]


# solution 1.
new_dict = {}

for blood_type in blood_types:
    if blood_type in new_dict:
        new_dict[blood_type] += 1
    
    else:
        new_dict[blood_type] = 1

print(new_dict)

# solution 2.
new_dict = {}

for blood_type in blood_types:
    new_dict[blood_type] = new_dict.get(blood_type, 0) + 1

print(new_dict)

# solution 3.
new_dict = {}

for blood_type in blood_types:
    new_dict.setdefault(blood_type, 0)
    new_dict[blood_type] += 1

print(new_dict)

# solution 4.
from collections import Counter

blood_types = ["A", "B", "A", "O", "AB", "AB", "O", "A", "B", "O", "B", "AB"]

new_dict = Counter(blood_types)

print(new_dict)
'''

# 2

'''
list1 = [1, 2, 3]
list2 = [4, 5, 6, 7, 8, 9]
set1 = set(list1)
set2 = set(list2)

# 1. add 4 to set1
set1.add(4)
print(set1) # {1, 2, 3, 4}

# 2. add [5, 6, 7] to set1
set1.update([5, 6, 7])
print(set1) # {1, 2, 3, 4, 5, 6, 7}

# 3. remove 7 from set1 (in two ways)
set1.remove(7) # set1.discard(7)
print(set1) # {1, 2, 3, 4, 5, 6}

# 4. set1 difference set2 (in two ways)
print(set1 - set2) # {1, 2, 3}
print(set1.difference(set2)) # {1, 2, 3}

# 5. set1 intersection set2 (in two ways)
print(set1 & set2) # {4, 5, 6}
print(set1.intersection(set2)) # {4, 5, 6}

# 6. set1 union set2 (in two ways)
print(set1 | set2) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(set1.union(set2)) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
'''

# 3

'''
# set1.pop() -> pop from the smallest memory address
set1 = {1, 2, 3, 4}

print(id(1))
print(id(2))
print(id(3))
print(id(4))

print(set1.pop())
print(set1.pop())
print(set1.pop())
print(set1)
'''

# 4

'''
# english dictionary
english_dictionary = {
    "plus" : ["더하기", "장점"], 
    "minus" : ["빼기", "적자"], 
    "multiply" : ["곱하기", "다양하게"], 
    "division" : ["나누기", "분열"]
}

# 1. english to korean (in three ways)
word = input()
print(english_dictionary[word])
print(english_dictionary.get(word))
print(english_dictionary.setdefault(word))

# 2. print words in dictionary
for key in english_dictionary.keys():
    print(key, end = " ")

print()

# 3. add word in dictionary (in three ways)
english_dictionary["square"] = ["제곱", "사각형"]
english_dictionary.setdefault("square", ["제곱", "사각형"])
english_dictionary.update({"square" : ["제곱", "사각형"]})

print(english_dictionary)

# 4. delete word from dictionary (in two ways)
word = input()
english_dictionary.pop(word)

print(english_dictionary)

word = input()
del english_dictionary[word]

print(english_dictionary)
'''

# 5

'''
# 1. assignment
list1 = [1, 2, 3, 4]
list2 = list1
list2[0] = 5

print(list1) # [5, 2, 3, 4]
print(id(list1)) # 2211417593408
print(list2) # [5, 2, 3, 4]
print(id(list2)) # 2211417593408

# 2. shallow copy (slicing, copy) => object in object : mutable
list1 = [1, 2, [3, 4]]
list2 = list1.copy() # list2 = list1[:]

list2[0] = 5
list2[2][0] = 5

print(list1, list2) # [1, 2, [5, 4]] [5, 2, [5, 4]]
print(id(list1), id(list2)) # 3044786378240 3044786339200
print(id(list1[2]), id(list2[2])) # 3044786378624 3044786378624

# 3. deep copy
import copy
list1 = [1, 2, [3, 4]]
list2 = copy.deepcopy(list1)

list2[2][0] = 5

print(list1, list2) # [1, 2, [3, 4]] [1, 2, [5, 4]]
print(id(list1), id(list2)) # 2338677171264 2338677139328
print(id(list1[2]), id(list2[2])) # 2338677920320 2338677138688
'''

# 6

