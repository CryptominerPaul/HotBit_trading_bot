###################################################
#  HotBit Exchange Bot Created by Cryptominer8245 #
#       Marker Maker, WashTrade & Info Bot        #
#                Created 2-22-2023                #
###################################################
import hotbit
from hotbit import Hotbit
from hotbit import reverseApi
import requests
import json
import time
import datetime
import random
import os
import termcolor
import hmac
import hashlib
from prettytable import PrettyTable
from termcolor import colored
from dotenv import load_dotenv
os.system('clear')
while True:
    load_dotenv()

    api_key = os.getenv("api_key")
    secret_key = os.getenv("secret_key")

    auth = hotbit.auth.api(api_key, secret_key)
    client = hotbit.Hotbit(auth)
#############################################################
# Get current date and time
    now = datetime.datetime.now()
    date_string = now.strftime("%B %d %Y")
    time_string = now.strftime("%I:%M:%S %p")
#############################################################
    symbol = os.getenv("symbol")
    base = os.getenv("base")
    pair = f"{symbol}{base}"
    market = f"{symbol}/{base}"
    markets = f"{symbol}/{base}"
    offset = 0
    limit = 10
    interval = 30
    print(colored("   HotBit Exchange Bot Loading   \n", "light_magenta"))

    time.sleep(1)
    try:
        depth = client.depthQuery(market)
    except Exception as e:
        print(f"Exception occurred: {e}")
        time.sleep(5)
        continue
##########_Server_Time__##########
    def get_server_time(servertime):
        output = termcolor.colored("Server Time:", "light_blue") + " " + str(servertime['result']) + "\n"
        return output

    server_time = client.serverTime()
    print(get_server_time(server_time))
    time.sleep(1)

##########_GET_CURRENT_BIDS_&_OFFERS_##########
#############################################################
# To get The rest of the working Code you must contact me  
# for Purchasing it - Thank you
