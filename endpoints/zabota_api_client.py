import requests
from endpoints.base_client import BaseClient


class ZabotaApiClient(BaseClient):
    def __init__(self, host):
        self.host = host

    def new_lead(self, data, status=200):
        response = requests.post(f"{self.host}/active/lead", json=data)
        self.check_status(response=response, status=status)
        return response.json()

    def get_active_all(self, status=200):
        response = requests.get(f"{self.host}/active")
        self.check_status(response=response, status=status)
        return response.json()

    def get_active_id(self, status=200):
        response = requests.get(f"{self.host}/active")
        self.check_status(response=response, status=status)
        list = response.json()
        active_id = list["items"][0]["id"]
        # как тут написать проверку, мол если у этого id тип бзе записи, проверь след id
        return active_id


    def get_active(self, active_id, status=200):
        response = requests.get(f"{self.host}/active/{active_id}")
        self.check_status(response=response, status=status)
        return response.json()

    def get_tour(self, tour_id, status=200):
        response = requests.get(f"{self.host}/tour/{tour_id}?expand=gallery,additionalProduct,ticketType,placeStart,paymentType,timetable,routeBlock,included,category")
        self.check_status(response=response, status=status)
        return response.json()


    def new_order(self, data, tour_id, status=200):
        response = requests.post(f"{self.host}/tour/{tour_id}/create-order", json=data)
        self.check_status(response=response, status=status)
        return response.json()
