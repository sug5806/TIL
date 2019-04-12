import sys

sys.stdin = open("bus_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    KNM  = list(map(int, input().split()))
    # K = 3 한번에 이동 가능한 수
    # N = 10  전체 정류장 갯수
    # M = 5 설치하는 충전소 갯수
    charge_num = list(map(int, input().split()))
    bus_stop = [ 0 for _ in range(KNM[1]+1)]

    for i in range(KNM[2]):
        bus_stop[charge_num[i]] = 1
        
    check = True
    cur_locate = 0
    charge_count = 0
    
    while check:
        if cur_locate + KNM[0] >= KNM[1]:
            break
        
        elif bus_stop[cur_locate + KNM[0]] == 1:
            cur_locate += KNM[0]
            charge_count += 1
            
        else:
            for i in range(cur_locate + (KNM[0]-1), cur_locate, -1):
                check = False
                if bus_stop[i] == 1:
                    cur_locate = i
                    charge_count += 1
                    check = True
                    break
            if not check:
                charge_count = 0
            
    print(f'#{test_case} {charge_count}')
    
    # ///////////////////////////////////////////////////////////////////////////////////
