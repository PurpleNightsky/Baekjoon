N = int(input())

dic = {}
chat = 0

for _ in range(N):
    user = input()

    if user == "ENTER":     #문자열 ENTER인 경우
        for key, value in dic.items():    #딕셔너리 순회
            if value == 1:   #값이 1인 (사용하지 않은) 항목을 찾음
                chat += 1   #chat 1 증가
        dic = {}   #딕셔너리 초기화

    else:
        if user not in dic:   #명령어가 딕셔너리에 없는 경우
            dic[user] = 1     #딕셔너리에 추가하고 값 1로 설정

for key, value in dic.items():
    if value == 1:
        chat += 1

print(chat)  #최종 결과 출력