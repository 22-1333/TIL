# 1

'''
print(help(list))

"""
Help on class list in module builtins:

class list(object)
 |  list(iterable=(), /)
 |
 |  Built-in mutable sequence.
 |
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |
 |  Methods defined here:
"""
'''

# 2

'''
numbers = [1, 2, 3]

# 1. assingment
list1 = numbers

# 2. slicing
list2 = numbers[:]

numbers[0] = 100

print(list1) # [100, 2, 3]
print(list2) # [1, 2, 3]
'''

# 3

'''
a = "Practice makes perfect"

# 1. 문자열 a에서 "e"의 개수 세기
print(a.count("e"))
# 2. 문자열 a에서 "i"의 위치 찾기(2가지 방법)
print(a.index("i"))
print(a.find("i"))
# 3. 문자열 a의 문자 사이에 . 삽입
print((".".join(a)))
# 4. 문자열 a를 공백 기준으로 분리하여 출력
print(a.split())
# 5. 문자열 a에서 'makes'를 'made'로 바꿔서 출력
a.replace("makes", "made")
# 6. 문자열 a를 대문자와 소문자로 변환하여 출력
print(a.lower())
# 7. 문자열 a에서 양쪽 공백 삭제하기
print(a.strip())
'''

# 4

'''
a = ["b", "a", "n", "a", "n"]

# 반환 하지 않는 메서드 -> 주로 원본을 변경한다.
# 1. 리스트 a의 마지막에 "a" 추가하기
a.append("a")
print(a)

# 2. 리스트 a를 오름차순으로 정렬
a.sort()
print(a)

print(sorted(a))

# 3. 리스트 a를 내림차순으로 정렬
a.sort(reverse = True)
print(a)

# 4. 리스트 a를 역순으로 뒤집기
a.reverse()
print(a)

# 5. 리스트 a에서 문자 "a" 삭제하기
a.remove("a")
print(a)

# 반환 하는 메서드 -> 주로 원본을 변경하지 않는다.
# 6. 리스트 a의 마지막 요소를 꺼내서 삭제하고 삭제한 요소 출력
print(a.pop())

# 7. 리스트 a에서 문자 "n"의 개수를 출력
print(a.count("n"))
'''