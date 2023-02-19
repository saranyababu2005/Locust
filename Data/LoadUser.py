import csv
import json
import os


class AddUsers:

    id_list=[]
    booking_list = []

    @staticmethod
    def load_users():
        reader = csv.DictReader(open(os.getcwd() + "/Data/user.csv"))

        for line in reader:
            AddUsers.id_list.append(line)

    @staticmethod
    def load_booking():
        with open(os.getcwd() + "/Data/BookingDetails.json",'r') as booking_details:
            # booking_details = open(os.getcwd() + "/Data/BookingDetails.json")
            data_reader =json.load(booking_details)
        print(data_reader)
        print(type(data_reader))
        for item in data_reader:
            AddUsers.booking_list.append(item)
            print(item)
        # print(AddUsers.booking_list)

    @staticmethod
    def get_User():
        if len(AddUsers.id_list) < 1:
            AddUsers.load_users()
        return AddUsers.id_list.pop()

    @staticmethod
    def get_BookingOrder():
        if len(AddUsers.booking_list) < 1:
            AddUsers.load_booking()
        return AddUsers.booking_list.pop()
