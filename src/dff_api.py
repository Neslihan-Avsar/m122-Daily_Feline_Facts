import requests
import json
import configparser
import sys
import re
import random
import math
import os
from datetime import datetime

# DEBUG MACROS DEFAULT

allowDebug = 'true'
allowWarning = 'true'
allowErrors = 'true'
allowLogging = 'true'

def debugLog(message):
    if allowDebug == 'true':
        print("DEBUG: ", message)

def warningLog(message):
    if allowWarning == 'true':
        print("WARNING: ", message)

def errorLog(message):
    if allowErrors == 'true':
        print("ERROR: ", message)

def exitSystemNoMessage(exit_code):
    if allowLogging == 'true':
        try:
            assert os.path.exists("dff_logging.log")
        except:
            print("Logging file is missing, please run \'dff_setup.py\' to create a new one or move the file to the same directory.")
            quit()
        timestamp = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
        log = open('dff_logging.log', 'a')
        log.write("\nTIMESTAMP: " + timestamp)
        log.write("\nCODE: " + str(exit_code) + "\n")
        log.close()
    quit()
# 0 = success, 1 = general failiure, 2 = config failiure, 3 = get failiure, 4 = post failiure, 5 = log failiure (theoretically)

def exitSystem(exit_code, message):
    if allowLogging == 'true':
        try:
            assert os.path.exists("dff_logging.log")
        except:
            print("Logging file is missing, please run \'dff_setup.py\' to create a new one or move the file to the same directory.")
            quit()
        timestamp = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
        log = open('dff_logging.log', 'a')
        log.write("\nTIMESTAMP: " + timestamp)
        log.write("\nCODE: " + str(exit_code))
        log.write("\nMESSAGE: " + message + "\n")
        log.close()
    quit()
# 0 = success, 1 = general failiure, 2 = config failiure, 3 = get failiure, 4 = post failiure, 5 = log failiure (theoretically)

# CONFIG FILE AND VARIABLE SETUP

try:
    assert os.path.exists("dff_config.cfg")
except:
    print("Config file is missing, please run \'dff_setup.py\' to create a new one or move the file to the same directory.")
    exitSystem(1)

CONFIG = configparser.ConfigParser()

CONFIG.read('dff_config.cfg')

# DEBUG CONFIG

allowDebug = CONFIG.get('DEV', 'allowdebugmessages')
allowWarning = CONFIG.get('DEV', 'allowwarningmessages')
allowErrors = CONFIG.get('DEV', 'allowerrormessages')
allowLogging = CONFIG.get('DEV', 'logprocess')

if allowDebug != 'true' and allowDebug != 'false' or allowWarning != 'true' and allowWarning != 'false' or allowErrors != 'true' and allowErrors != 'false':
    print("At least one of dff_config.cfg/DEV/* is neither \'true\' nor \'false\'.")
    exitSystem(2)

if allowLogging != 'true' and allowLogging != 'false':
    print("The logging boolean is neither \'true\' or \'false\'.")
    exitSystem(2)

URL = CONFIG.get('API Website', 'url')
_IMAGE = CONFIG.get('API Website', 'image')
_TIMEOUT_API = CONFIG.get('API Website', 'timeout_api')
JSON_PATH = CONFIG.get('API Website', 'json_path')
STATUSCODE_API = CONFIG.get('API Website', 'display_statuscode_api')

TOKEN = CONFIG.get('Discord WebHook', 'token')
_TIMEOUT_WEBHOOK = CONFIG.get('Discord WebHook', 'timeout_webhook')
STATUSCODE_WEBHOOK = CONFIG.get('Discord WebHook', 'display_statuscode_webhook')
CONTENT = CONFIG.get('Discord WebHook', 'content_message')
_COLOR = CONFIG.get('Discord WebHook', 'color')

# API WEBSITE

if re.search("^(http\:\/\/){1}(.+)(\.[a-zA-Z]{2,3})(\/.+)+$", URL) == True:
    warningLog("dff_config.cfg/API Website/url may not be secure, as it uses http://.")
elif re.search("^(https?\:\/\/){1}(.+)(\.[a-zA-Z]{2,3})(\/.+)$", URL) == False:
    message = "dff_config.cfg/API Website/url is not a valid URL."
    errorLog(message)
    exitSystem(2, message)
else:
    debugLog("url is using https protocol and is a valid url.")

if math.isnan(float(_TIMEOUT_API)):
    message = "dff_config.cfg/API Website/timeout_api is either empty or not a number."
    errorLog(message)
    exitSystem(2, message)
else:
    TIMEOUT_API = float(_TIMEOUT_API)

if _IMAGE == "":
    warningLog("dff_config/API Website/image is empty.")
else:
    random =  str(random.randint(225, 255))
    IMAGE = _IMAGE + "?width\=" + random + "&height\=" +  random

JSON = requests.get(URL, timeout=TIMEOUT_API)
FACT = JSON.json().get(JSON_PATH)

if str(JSON.status_code)[0]!= '2':
    message = "get request was unsuccessful."
    errorLog(message)
    exitSystem(3, message)

if STATUSCODE_API == 'true':
    print('Status Code of the API GET Request: ', JSON.status_code)
elif STATUSCODE_API != 'false':
    message = "dff_config.cfg/API Website/display_statuscode_api is neither \'true\' or \'false\'."
    errorLog(message)
    exitSystem(2, message)

# DISCORD WEBHOOK

if re.search("^https://discord.com/api/webhooks/.*$", TOKEN) == False:
    message = "dff_config.cfg/Discord WebHook/token is invalid. Please make sure it starts with \'https://discord.com/api/webhooks/\'."
    errorLog(message)
    exitSystem(2, message)

if math.isnan(float(_TIMEOUT_WEBHOOK)):
    message = "dff_config.cfg/Discord WebHook/timeout_webhook is either empty or not a number."
    errorLog(message)
    exitSystem(2, message)
else:
    TIMEOUT_WEBHOOK = float(_TIMEOUT_WEBHOOK)

if math.isnan(int(_COLOR)):
    message = "dff_config.cfg/Discord WebHook/color is either empty or not a number."
    errorLog(message)
    exitSystem(2, message)
else:
    COLOR = int(_COLOR)

POST = {"content": CONTENT, "embeds": [{"description": FACT, "color": COLOR, "image":{"url": IMAGE}}], "attachments": []}
HEADER = {'Content-Type': 'application/json'}
RESPONSE = requests.post(TOKEN, headers=HEADER, data=json.dumps(POST), timeout=TIMEOUT_WEBHOOK)

if str(RESPONSE.status_code)[0]!= '2':
    message = "post request was unsuccessful."
    errorLog(message)
    exitSystem(4, message)

if STATUSCODE_WEBHOOK == 'true':
    print('Status Code of the WebHook POST Request: ', RESPONSE.status_code)
elif STATUSCODE_WEBHOOK != 'false':
    message = "dff_config.cfg/Discord WebHook/display_statuscode_webhook is neither \'true\' or \'false\'."
    errorLog(message)
    exitSystem(2, message)

exitSystemNoMessage(0)
