N = int(input())   #N입력
if N == 0 :
    print(1)
else :
    result = 1   #1로 초기화
    for i in range(2, N+1) :   #2~N+1 까지 반복
        result = result*i   #i를 result에 곱함
    print(result)