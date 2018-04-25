#! /usr/bin/python3
import socket
import threading
from queue import Queue

print_lock = threading.Lock()
target_website = input('Specify the website to connect: ')


def portscan(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connection = sock.connect((target, port))
        with print_lock:
            print('Port {} is open!'.format(str(port)))
        connection.close()
    except:
        pass


def threader():
    while True:
        worker = queue.get()
        portscan(worker)
        queue.task_done()


queue = Queue()

for worker in range(300):
    thread = threading.Thread(target=threader)
    thread.daemon = True
    thread.start()

for task in range(1, 10000):
    queue.put(task)

queue.join()
