# WON'T WORK IN WINDOWS DUE TO os.fork()
import os


def child_process():
    print(f"child process PID: {os.getpid()}")
    print("EXIT CHILD ")


def parent_process():
    print(f"parent process PID: {os.getpid()}")
    child_pid = os.fork()
    if child_pid == 0:
        child_process()
    else:
        print("PARENT")
        print(f"child process PID is: {child_pid}")

    while True:
        pass


parent_process()
