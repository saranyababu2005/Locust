
from locust import TaskSet,task


class Task1(TaskSet):

    @task
    def get_admin_token(self):
        #     # token_id = ''
        token_id = self.user.give_token()
        auth_headers = {"Content-Type": "application/json", "Accept": "application/json",
                        "Cookie": "token={}".format(token_id)}
        self.client.put('/booking/289', headers=auth_headers, json=
        {
            "firstname": "heloo",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        })