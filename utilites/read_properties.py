import configparser


config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")


class ReadConfig():
    @staticmethod
    def get_application_url():
        url = config.get('login info', 'url')
        return url

    @staticmethod
    def get_application_email():
        email = config.get('login info', 'email')
        return email

    @staticmethod
    def get_application_password():
        password = config.get('login info', 'password')
        return password
