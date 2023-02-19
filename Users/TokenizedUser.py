from locust import HttpUser,wait_time,between
import csv
import os
from Data.LoadUser import AddUsers

class UserA(HttpUser):

    wait_time=between(1,2)
    abstract = True

    def __init__(self,parent):
        super(UserA, self).__init__(parent)
        self.token_id = ''
        self.user_obj = {}
        # self.userid=''

    def on_start(self):
        self.user_obj = AddUsers.get_User()

        self.userid = self.user_obj['username']
        print(self.userid)
        self.pwd= self.user_obj['password']
        print(self.pwd)

        data1 = {"username": self.userid, "password": self.pwd}
        response = self.client.post('/auth', data1 )
        tokens = response.json()
        print(tokens['token'])
        self.token_id = tokens['token']

    def give_token(self):
        return self.token_id





