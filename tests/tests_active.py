import pytest

@pytest.mark.usefixtures("api")
class TestActive:
    def test_lead(self, api, db):
    #отправка заявки на занятие
        res = db.get_id()
        active_id = res["id"]
        data = {
            "active_id": active_id,
            "name": "Иван",
            "phone": "79000000000",
            "date": "2025-02-27 11:00-11:30"
        }
        response = api.new_lead(data=data)
        assert response == 'Заявка отправлена'

        list_lead = db.get_lead_id()
        lead_id = list_lead["id"]
        db.delete_id(lead_id)

    def test_lead_negative(self, api, db):
        #запись на занятие с типом "без записи"
        res = db.get_id(2)
        active_id = res["id"]
        data = {
            "active_id": active_id,
            "name": "Иван",
            "phone": "79000000000",
            "date": "2025-02-27 11:00-11:30"
        }
        response = api.new_lead(data=data, status=500)
        assert response["message"] == 'У этой актиновности тип без записи'
