# weekly test 01

"""
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 왼쪽 위 좌표(r1, c1), 오른쪽 아래 좌표(r2, c2)
    r1, c1, r2, c2 = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sumV = 0

    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            # 해당 좌표값의 합계
            sumV += arr[i][j]
    # 전체 합을 구역의 크기로 나누기 -> 평균
    avgV = sumV // ((r2 - r1 + 1) * (c2 - c2 + 1))
    result = 0
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            avgV_abs = arr[i][j] - avgV
            if avgV_abs < 0:
                avgV_abs *= -1
            result += avgV_abs

    print(f"#{tc} {result}")

"""

# weekly test 02

"""
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = 0
    # N번의 바운스 챌린지
    for i in range(N):
        # 첫번째 바운스부터 N번째 바운스까지, 각 바운스는 i + 1 씩 인덱스 증가
        for j in range(0, N, i + 1):
            result += numbers[j]
    # result 가 0 보다 작으면 0으로 변경
    result = result if result >= 0 else 0
    print(f"#{tc} {result}")
"""

# weekly test 03

"""
while start <= end:
    middle = (start + end) // 2
    # 검색 성공
    if a[middle] == key:
        return True
    elif a[middle] > key:
        end = middle - 1
    else:
        start = middle + 1
    
# 검색 실패
return False
"""

# extra_pro_1

"""
# 1
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))

    cnt = 0
    result = 0

    for i in range(N):
        if passcode[cnt] == sample[i]:
            cnt += 1
        if cnt == K:
            result = 1
            break
    print(f"#{tc} {result}")
    
# 2
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    sample = list(map(int, input().split()))
    passcode = list(map(int, input().split()))

    indexes = []
    result = 1
    
    for i in range(len(passcode)):
        now = passcode[i]
        try:
            index = sample.index(now)
            sample = sample[index + 1 : ]
        except:
            result = 0
    print(f"#{tc} {result}")
"""
