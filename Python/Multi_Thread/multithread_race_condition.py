import threading as th
# race condition

# 해결책!
# mutual exclusion(상호 배제)

# 공유 자원(shared resource)
g_num = 0
lock = th.Lock()


def thread_main():
    global g_num
    # critical section
    # 스레드가 공유 자원에 접근은 괜찮음
    # 공유 자원을 수정하려고 하는 코드
    lock.acquire()
    for _ in range(100000):
        g_num += 1
    lock.release()

threads = []

for i in range(50):
    # TCB 만들고 등등 여러작업을 하기때문에 리소스를 많이잡아먹음
    threads.append(th.Thread(target = thread_main))

for tt in threads:
    tt.start()

for tt in threads:
    tt.join()


print(f'g_num : {g_num:,}')
