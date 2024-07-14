import threading
import time


def worker_thread(id_val):
    print(f"Thread ID {id_val} now alive")
    count = 1
    while True:
        print(f"Thread with id {id_val} has counter value {count}")
        time.sleep(2)
        count += 1


# Create threads
for i in range(5):
    thread = threading.Thread(target=worker_thread, args=(i,))
    thread.start()

print("Main thread - infinite wait loop")
while True:
    pass
