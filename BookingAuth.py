from locust import task, TaskSet, HttpUser, between
from Users.TokenizedUser import UserA

class GetToken(TaskSet):



    @task
    def get_admin_token(self):
    #     # token_id = ''


    # def get_booking_ids(self):
    #     response = self.client.get('/booking')
    #     print(response.text)
    #
    # def get_booking_id(self):
    #     response = self.client.get('/booking/5839')
    #     print(response.text)
    #
    # @task
    # def update_booking_id(self):
    #     self.client.headers['Content-Type']= 'application/json'
    #     self.client.headers['Cookie'] = 'token=f7c9a2bb97d0267'
    #     user = UserA()
        self.token_id=self.user.give_token()
        auth_headers = {"Content-Type": "application/json","Accept": "application/json","Cookie": "token={}".format(self.token_id)}
        self.client.put('/booking/289',headers = auth_headers, json=
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


class Auth(HttpUser):
    wait_time = between(1, 2)
    tasks = [GetToken]
