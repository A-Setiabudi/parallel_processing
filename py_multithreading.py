import threading
import time

def hitung(n, sleep_time):
    for i in range (1, n+1):
        print(i)
        time.sleep(sleep_time)

for a in range(1,4):
    x = threading.Thread(target=hitung, args=(10,a,))
    x.start()
print('active threading: ', threading.active_count())

