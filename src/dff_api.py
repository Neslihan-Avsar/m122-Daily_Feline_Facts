import requests
import json
import configparser
import sys
import re
import math
from datetime import datetime

# DEBUG MACROS DEFAULT

allowDebug = True
allowWarning = True
allowErrors = True
allowLogging = True

def debugLog(message):
    if allowDebug:
        print("DEBUG: ", message)

def warningLog(message):
    if allowWarning:
        print("WARNING: ", message)

def errorLog(message):
    if allowErrors:
        print("ERROR: ", message)

def exitSystem(exit_code):
    if allowLogging == 'true':
        timestamp = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
        log = open('dff_logging.log', 'a')
        log.write("\nTIMESTAMP: " + timestamp)
        log.write("\nCODE: " + str(exit_code) + "\n")
        log.close()
    quit()
# 0 = success, 1 = general failiure, 2 = config failiure, 3 = get failiure, 4 = post failiure, 5 = log failiure

# CONFIG FILE AND VARIABLE SETUP

CONFIG = configparser.ConfigParser()

CONFIG.read('dff_config.cfg')
debugLog("config file was read")

# DEBUG CONFIG

allowDebug = CONFIG.get('DEV', 'allowDebugMessages')
allowWarning = CONFIG.get('DEV', 'allowWarningMessages')
allowErrors = CONFIG.get('DEV', 'allowErrorMessages')
allowLogging = CONFIG.get('DEV', 'logProcess')

if allowDebug != 'true' and allowDebug != 'false' or allowWarning != 'true' and allowWarning != 'false' or allowErrors != 'true' and allowErrors != 'false':
    print("At least one of dff_config.cfg/DEV/* is neither \'true\' nor \'false\'.")
    exitSystem(2)

if allowLogging != 'true' and allowLogging != 'false':
    print("The logging boolean is neither \'true\' or \'false\'.")
    exitSystem(2)

URL = CONFIG.get('API Website', 'url')
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
    errorLog("dff_config.cfg/API Website/url is not a valid URL.")
    exitSystem(2)
else:
    debugLog("url is using https protocol and is a valid url.")

if math.isnan(float(_TIMEOUT_API)):
    errorLog("dff_config.cfg/API Website/timeout_api is either empty or not a number.")
    exitSystem(2)
else:
    TIMEOUT_API = float(_TIMEOUT_API)

JSON = requests.get(URL, timeout=TIMEOUT_API)
FACT = JSON.json().get(JSON_PATH)

if STATUSCODE_API == 'true':
    print('Status Code of the API GET Request: ', JSON.status_code)
elif STATUSCODE_API != 'false':
    errorLog("dff_config.cfg/API Website/display_statuscode_api is neither \'true\' or \'false\'.")
    exitSystem(2)

# DISCORD WEBHOOK

if re.search("^https://discord.com/api/webhooks/.*$", TOKEN) == False:
    errorLog("dff_config.cfg/Discord WebHook/token is invalid. Please make sure it starts with \'https://discord.com/api/webhooks/\'.")
    exitSystem(2)

if math.isnan(float(_TIMEOUT_WEBHOOK)):
    errorLog("dff_config.cfg/Discord WebHook/timeout_webhook is either empty or not a number.")
    exitSystem(2)
else:
    TIMEOUT_WEBHOOK = float(_TIMEOUT_WEBHOOK)

if math.isnan(int(_COLOR)):
    errorLog("dff_config.cfg/Discord WebHook/color is either empty or not a number.")
    exitSystem(2)
else:
    COLOR = int(_COLOR)

POST = {"content": CONTENT, "embeds": [{"description": FACT, "color": COLOR}], "attachments": []}
HEADER = {'Content-Type': 'application/json'}
RESPONSE = requests.post(TOKEN, headers=HEADER, data=json.dumps(POST), timeout=TIMEOUT_WEBHOOK)

if STATUSCODE_WEBHOOK == 'true':
    print('Status Code of the WebHook POST Request: ', RESPONSE.status_code)
elif STATUSCODE_WEBHOOK != 'false':
    errorLog("dff_config.cfg/Discord WebHook/display_statuscode_webhook is neither \'true\' or \'false\'.")
    exitSystem(2)

exitSystem(0)
