import time
from threading import Thread

def sleepMe(i):
    print(f"Поток {i} засыпает на 5 секунд.")
    time.sleep(5)
    print(f"Поток {i} сейчас проснулся.")

for i in range(1):
    th = Thread(target=sleepMe, args=(i, ))
    th.start()