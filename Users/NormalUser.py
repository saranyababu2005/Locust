from locust import HttpUser,wait_time,between

from Data.LoadUser import AddUsers


class GeneralUser(HttpUser):

    wait_time = between(1,2)
    abstract = True

    def on_start(self):
        # self.bookingDetails = AddUsers.get_BookingOrder()
        self.bookingData = AddUsers.get_BookingOrder()
        print(self.bookingData)

    def giveBookingData(self):
        return self.bookingData


