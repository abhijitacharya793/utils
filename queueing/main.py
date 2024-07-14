# Explore thread lock and multiprocessing

import threading
import queue
import time


class WorkerThread(threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q

    def run(self):
        # Port scanner/password cracking/etc
        print("In WorkerThread")
        while True:
            counter = self.q.get()
            print(f"Ordered to sleep for {counter} seconds")
            time.sleep(counter)
            print(f"Finished sleeping for {counter} seconds")
            self.q.task_done()


q = queue.Queue()

for i in range(10):
    print(f"Creating WorkerThread : {i}")
    worker = WorkerThread(q)
    worker.daemon = True
    worker.start()
    print(f"WorkerThread {i} created")

for j in range(10):
    q.put(j)

q.join()

print("All tasks over!")
