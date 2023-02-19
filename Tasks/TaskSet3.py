from locust import TaskSet, task, SequentialTaskSet


class Task3(SequentialTaskSet):
    #
    # def __init__(self):
    #     self.booking_id = ''

    @task
    def createBooking(self):
        bookingData = self.user.giveBookingData()
        print(bookingData)
        auth_headers = {"Content-Type": "application/json", "Accept": "application/json"}
        response = self.client.post('/booking', headers=auth_headers, json=bookingData)
        response_json=response.json()
        self.booking_id = response_json['bookingid']

    @task
    def getBookingDetails(self):
        response = self.client.get('/booking/{}'.format(self.booking_id))
        print(response.text)
