
import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getAppURL():
        url = config.get('common info', 'baseURL')
        return url
    @staticmethod
    def getUserEmail():
        email= config.get('common info', 'email')
        return email

    @staticmethod
    def getUserPassword():
        password = config.get('common info', 'password')
        return password
