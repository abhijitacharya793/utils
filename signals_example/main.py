# signals

import signal


def ctrlc_handler(signum, frm):
    print("You can not kill this")


print("Exploring signal handler")
signal.signal(signal.SIGINT, ctrlc_handler)
print("DONE!!")

while True:
    pass
