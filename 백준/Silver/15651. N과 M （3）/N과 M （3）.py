N, M = list(map(int, input().split()))   #N과 M을 입력
# 리스트로 만듦(분리된 문자열 정수 변환(int(input().공백기준 분리)))

listA = []   #수열을 저장할 리스트

def dfs() :
    if len(listA) == M :   #수열의 길이 = M일때 M출력
        print(' '.join(map(str, listA)))
        return

    for i in range(1, N+1) :   #1~N 까지
        listA.append(i)    #listA에 원소 i 추가
        dfs()   #재귀호출
        listA.pop()   #백트래킹 --> 이전으로 돌아감 -> 마지막 요소 제거

dfs()   #dfs 함수 호출