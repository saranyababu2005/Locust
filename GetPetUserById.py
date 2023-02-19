from locust import HttpUser,wait_time,between,task,TaskSet,events
import csv
import os


class GetById(TaskSet):

    id_list = []

    @staticmethod
    def load_users():
        reader = csv.DictReader(open(os.getcwd() + "/petid.csv"))
        for line in reader:
            GetById.id_list.append(line)

    @task
    def get_pet_user_by_id(self):
        id_details = GetById.get_one_user()
        response = self.client.get('/pet/{}'.format(id_details['id']))
        print(response.text)

    @staticmethod
    def get_one_user():
        if len(GetById.id_list) < 1:
            GetById.load_users()
        return GetById.id_list.pop()


class Users(HttpUser):


    wait_time = between(1,2)
    tasks = [GetById]





