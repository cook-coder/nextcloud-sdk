class NextcloudAPI:
    host = ''
    username:str
    password:str

    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password