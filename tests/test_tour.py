import pytest
from utils.data_prep.data_tour_order import generate_order_data

@pytest.mark.all_tests
@pytest.mark.tour
class TestTour:
    @pytest.mark.smoke
    def test_create_new_order(self, api, db):
        tour_id = db.get_first_tour_id()["id"]
        data = generate_order_data(api, db, tour_id)
        response = api.new_order(tour_id=tour_id, data=data)
        assert 'order_id' in response['success']['data']

    @pytest.mark.regress
    def test_negative_create_new_order(self, api, db):
        tour_id = db.get_first_tour_id()["id"]
        data = generate_order_data(api, db, tour_id)
        data["tickets"][0]["type_id"] = data["tickets"][0]["type_id"] - 1
        ticket_type_id = data["tickets"][0]["type_id"]
        response_tour = api.new_order(tour_id=tour_id, data=data)
        assert response_tour["errors"] == f"Тикет билета с ID {ticket_type_id} не найден"

