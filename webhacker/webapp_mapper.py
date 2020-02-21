import threading
import os
import requests
from queue import Queue


threads = 10
target = "http://www.blackhatpython.com"
directory = "/Users/justin/Downloads/joomla-3.1.1"
filters = [".jpg",".gif","png",".css"]

os.chdir(directory)

web_paths = Queue()

for r,d,f in os.walk("."):
    for files in f:
        remote_path = "%s/%s" % (r,files)
        if remote_path.startswith("."):
            remote_path = remote_path[1:]
        if os.path.splitext(files)[1] not in filters:
            web_paths.put(remote_path)


def test_remote():
    while not web_paths.empty():
        path = web_paths.get()
        url = "%s%s" % (target, path)

        res = requests.get(url)

        try:

            content = res.text

            print("[%d] => %s" % (res.encoding, path))
            res.close()
        except Exception as error:
            pass


# 多个进程同时对队列进行操作
for i in range(threads):
    print("Spawning thread: %d" % i)
    t = threading.Thread(target=test_remote)
    t.start()