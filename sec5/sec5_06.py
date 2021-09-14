'''
응급실
메디컬 병원 응급실에는 의사가 한 명밖에 없습니다.
응급실은 환자가 도착한 순서대로 진료를 합니다. 하지만 위험도가 높은 환자는 빨리 응급조
치를 의사가 해야 합니다. 이런 문제를 보완하기 위해 응급실은 다음과 같은 방법으로 환자의
진료순서를 정합니다.
• 환자가 접수한 순서대로의 목록에서 제일 앞에 있는 환자목록을 꺼냅니다.
• 나머지 대기 목록에서 꺼낸 환자 보다 위험도가 높은 환자가 존재하면 대기목록 제일 뒤로
다시 넣습니다. 그렇지 않으면 진료를 받습니다.
즉 대기목록에 자기 보다 위험도가 높은 환자가 없을 때 자신이 진료를 받는 구조입니다.
현재 N명의 환자가 대기목록에 있습니다.
N명의 대기목록 순서의 환자 위험도가 주어지면, 대기목록상의 M번째 환자는 몇 번째로 진료
를 받는지 출력하는 프로그램을 작성하세요.
대기목록상의 M번째는 대기목록의 제일 처음 환자를 0번째로 간주하여 표현한 것입니다.
▣ 입력설명
첫 줄에 자연수 N(5<=N<=100)과 M(0<=M<N) 주어집니다.
두 번째 줄에 접수한 순서대로 환자의 위험도(50<=위험도<=100)가 주어집니다.
위험도는 값이 높을 수록 더 위험하다는 뜻입니다. 같은 값의 위험도가 존재할 수 있습니다.
▣ 출력설명
M번째 환자의 몇 번째로 진료받는지 출력하세요.
▣ 입력예제 1
5 2
60 50 70 80 90
▣ 출력예제 1
3 ▣
입력예제 2
6 0
60 60 90 60 60 60
▣ 출력예제 2
5
'''

from collections import deque

n, m = map(int, input().split())
pain = list(map(int, input().split()))
queue = pain
count = 0

#m은 원하는 친구가 어디 있는지 기록.
while queue:
    #내가 원하는 순번의 친구가 진료를 받고 나간 경우.
    if m == -1:
        print(count)
        break

    length = len(queue)
    #맨 앞의 친구를 빼서
    pop = queue.pop(0)

    for i in range(len(queue)):
        if queue[i] > pop:
            # 뒤에 하나라도 우선순위가 급한애가 있으면 맨 뒤로 넣는다.
            queue.append(pop)
            m -= 1
            break

    # m이 진료를 못받고 다시 들어간 경우
    # -1인데 다시 들어갔다면 m을 queue의 맨 마지막 index로 해야함.
    if length == len(queue):
        m %= len(queue)

    # 진료를 받았다면 한명 빠진거니까 -1,
    # 총 몇 명이 받았는지 기록
    else:
        m -= 1
        count += 1


#강의 방법 : 그냥 index 번호를 같이 저장.
Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q = deque(Q)
cnt = 0
while True:
    pop = Q.popleft()
    if any(pop[1] < x[1] for x in Q):
        queue.append(pop)
    else:
        cnt += 1
        if pop[0] == m:
            print(cnt)
            break
