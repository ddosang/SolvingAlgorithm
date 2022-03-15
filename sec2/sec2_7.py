'''
소수(에라토스테네스 체)
자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요.
만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다.
제한시간은 1초입니다.

▣ 입력설명
첫 줄에 자연수의 개수 N(2<=N<=200,000)이 주어집니다.
▣ 출력설명
첫 줄에 소수의 개수를 출력합니다.
▣ 입력예제 1
20
▣ 출력예제 1
8
'''

n = int(input())
cnt = 0


#for 문 도는 방법. -> 시간 제한 초과
# for i in range(2, n+1):
#     for j in range(2 ,i):
#         if (i % j == 0):
#             break
#     else:
#         cnt += 1

#에라토스테네스 체

isPrime = [0] * (n+1)

for i in range(2, n+1):
    if isPrime[i] == 0:
        cnt += 1
        for j in range(i, n+1, i): #if문으로 따지지 말고 간격을 i로 두자.
            isPrime[j] = i

print(cnt)
