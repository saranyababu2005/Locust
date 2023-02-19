from locust import events

from Tasks.TaskSet1 import Task1
from Tasks.TaskSet2 import Task2
from Tasks.TaskSet3 import Task3
from Users.TokenizedUser import UserA
from Users.NormalUser import GeneralUser
# from CommonLib.EventHandlers import EventHandlers
# from CommonLib.EventInfluxHandlers import InfluxHandlerEvents

#
# class GroupA(UserA):
#
#     tasks = [Task1]


class GroupB(GeneralUser):
    # tasks = [Task2]
      tasks = [Task3]


@events.test_start.add_listener
def on_test_start(**kwargs):
    print("first one")
    # InfluxHandlerEvents.init_influx_client()

