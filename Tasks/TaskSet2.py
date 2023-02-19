from locust import TaskSet, task


class Task2(TaskSet):

    @task
    def getBooking(self):
        response = self.client.get('/booking/289')
        print(response.text)