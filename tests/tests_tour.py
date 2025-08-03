import pytest

@pytest.mark.usefixtures("api")
class TestTour:
    def test_create_new_order(self, api, db):
        res = db.get_tour_id()
        tour_id = res["id"]
        response = api.get_tour(tour_id=tour_id)
        first_timetable_id = response["timetable"][0]["id"]
        payment_type_id = response["paymentType"][0]["id"]
        place_start_id = response["placeStart"][0]["id"]
        ticket_type_id = response["ticketType"][0]["id"]
        #Тут наверное правильнее будет data куда то выносить и опрокидывать в параметры ?
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

    def test_negative_create_new_order(self, api, db):
        res = db.get_tour_id()
        tour_id = res["id"]
        response = api.get_tour(tour_id=tour_id)
        first_timetable_id = response["timetable"][0]["id"]
        payment_type_id = response["paymentType"][0]["id"]
        place_start_id = response["placeStart"][0]["id"]
        ticket_type_id = response["ticketType"][0]["id"] - 1

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
        response_tour = api.new_order(tour_id=tour_id, data=data)
        assert response_tour["errors"] == f"Тикет билета с ID {ticket_type_id} не найден"

