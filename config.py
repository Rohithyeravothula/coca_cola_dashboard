import configparser

config = configparser.ConfigParser()
config.read('../config.ini')

ms_api_subscription_key = config["Microsoft API"]["subscription_key"]
