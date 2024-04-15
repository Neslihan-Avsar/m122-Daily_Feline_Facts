import os
import configparser

if os.path.exists("dff_logging.log"):
    print("Logging file has already been created.")
else :
    log = open("dff_logging.log", 'w')
    log.write("LOG FILE OF DAILY FELINE FACTS\n------------------------------\n")
    log.close()

if os.path.exists("ddf_config.cfg"):
    print("Config file has already been created.")
    quit()

cfg = configparser.ConfigParser()
cfg['DEV'] = {
    'allowdebugmessages' : 'false',
    'allowwarningmessages' : 'false',
    'allowerrormessages' : 'false',
    'logprocess' : 'true'
}
cfg['API Website'] = {
    'url' : 'INSERT YOUR API HERE',
    'image' : 'INSERT YOUR API HERE',
    'timeout_api' : '2.0',
    'json_path' : 'INSERT YOUR JSON VALUE HERE',
    'display_statuscode_api' : 'true'
}
cfg['Discord WebHook'] = {
    'token' : 'INSERT YOUR DISCORD WEBHOOK TOKEN HERE',
    'timeout_webhook' : '2.0',
    'display_statuscode_webhook' : 'true',
    'content_message' : 'INSERT YOUR MESSAGE HERE',
    'color' : '6580991'
}
with open("dff_config.cfg", 'w') as configfile:
    cfg.write(configfile)
    configfile.close()

quit()
