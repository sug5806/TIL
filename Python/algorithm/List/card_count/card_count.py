import sys
sys.stdin = open("card_count_sample_input.txt", "r")

T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    cnt = []
    card_li = []
    num = int(input())
    card_num = input()    
    idx = 0

    for i in card_num:
        card_li.append(i)
    cnt = [0 for _ in range(10)]

    for i in range(num):
        cnt[int(card_li[i])] += 1
    for i in range(9, 0,-1):
        if max(cnt) == cnt[i]:
            idx = i
            break

    print(f'#{test_case} {idx} {max(cnt)}')
    