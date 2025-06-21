import pytest
import requests
from endpoints.zabota_api_client import ZabotaApiClient

tour_id = 35

@pytest.mark.usefixtures("api")
class TestActive:
    def test_get_active_id(self, api):
        active_id = api.get_active_id()
        response = api.get_active(active_id=active_id)
        assert response["id"] == active_id

    def test_lead(self, api):
    #запись на занятие
        active_id = api.get_active_id()
        data = {
            "active_id": active_id,
            "name": "Иван",
            "phone": "79000000000",
            "date": "2025-02-27 11:00-11:30"
        }
        response = api.new_lead(data=data)
        assert response == 'Заявка отправлена'

    def test_lead_negative(self, api):
        #запись на занятие с типом "без записи"
        active_id = api.get_active_id()
        data = {
            "active_id": active_id,
            "name": "Иван",
            "phone": "79000000000",
            "date": "2025-02-27 11:00-11:30"
        }
        response = api.new_lead(data=data, status=500)
        assert response["message"] == 'У этой актиновности тип без записи'



class TestTour:
    def test_create_new_order(self, api):
        response = api.get_tour(tour_id=tour_id)
        first_timetable_id = response["timetable"][0]["id"]
        payment_type_id = response["paymentType"][0]["id"]
        place_start_id = response["placeStart"][0]["id"]
        ticket_type_id = response["ticketType"][0]["id"]

        data = {
                "timetable_id": first_timetable_id,
                "payment_type_id": payment_type_id,
                "place_start_id": place_start_id,
                "tickets": [
                    {
                        "type_id": ticket_type_id,
                        "count": 2
                    }
                ],
                "client_email": "testemail@mail.ru",
                "client_fio": "testfio",
                "client_telephone": "+79991234567",
                "url_success": "https://example.com/success",
                "url_fail": "https://example.com/fail"
            }
        # print(data)
        response_tour = api.new_order(tour_id=tour_id, data=data)
        assert 'order_id' in response_tour['success']['data']
