#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import argparse
import time
import random
import threading
import requests
from fake_useragent import UserAgent
from colorama import Fore

# in seconds
wait_between_request = 1
output_file = "available.txt"
# timeout of each requests
timeout_var = 10

main_web = "https://www.joinclubhouse.com/@"

"""
how to call this script:
threading and proxy is optional
python main.py -wordlist users.txt -threading 5 -proxy file.txt
"""
parser = argparse.ArgumentParser()
parser.add_argument('-wordlist', required=True, help="Item to check users")
parser.add_argument('-threading', required=False, help="Default 1")
parser.add_argument('-proxy', required=False, help="Select proxy file")
args = parser.parse_args()

def load_file():
    file_user = args.wordlist
    content=[]
    if os.path.isfile(file_user):
        with open(file_user) as f:
            content = f.readlines()
        content = [item.strip() for item in content]
        return content
    else:
        print ("Missing file:", file_user)
        exit()

def check_user(username,proxy_list):
    special_web = main_web + str(username)
    user_available=False
    try:
        # fake user agent
        ua = UserAgent()
        a = ua.random
        user_agent = ua.random
        headers= {'User-Agent':user_agent}
        if proxy_list:
            proxy_to_use = random.choice(proxy_list)
            proxyDict = {
              "http"  : proxy_to_use
            }

            response = requests.get(special_web, headers=headers, timeout=timeout_var, proxies=proxyDict)
        else:
            response = requests.get(special_web, headers=headers, timeout=timeout_var)

        if response.status_code == 404:
            user_available=True

    except:
        pass

    if user_available:
        print (Fore.GREEN + f"User: {username}")
        save_user_exist(username)
    else:
        print (Fore.RED + f"User: {username}")

def save_user_exist(username):
    with open(output_file, 'a+') as f:
        f.write(str(username) + "\n")

def load_proxy():
    if args.proxy:
        file_proxy = args.proxy
        content=[]
        if os.path.isfile(file_proxy):
            with open(file_proxy) as f:
                content = f.readlines()
                content = [item.strip() for item in content]
                return content
        else:
            print ("Missing file:", file_proxy)
            print ("Continue without proxy")
    else:
        print ("Continue without proxy")

    return []

def main():
    # load users
    user_list = load_file()

    # check if threading is used
    if args.threading:
        num_thread = int(args.threading)
    else:
        num_thread=1

    print (f"Working with {num_thread} threads")
    # try to load proxies
    proxy_list = load_proxy()

    for username in user_list:
        while threading.active_count() >= num_thread+1:
            time.sleep(1)
        thread = threading.Thread(target=check_user,args=(username,proxy_list))
        thread.setDaemon(True)
        thread.start()
        time.sleep(wait_between_request)



if __name__ == '__main__':
    main()
