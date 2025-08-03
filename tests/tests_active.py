from faker import Faker

class TestActive:
    def test_lead(self, api, db, fake):
    #отправка заявки на занятие
        res = db.get_first_active_id()
        active_id = res["id"]
        generated_name = fake.first_name_male()
        generated_phone = fake.phone_number()
        data = {
            "active_id": active_id,
            "name": generated_name,
            "phone": generated_phone,
            "date": fake.date_time_between(start_date="+1d", end_date="+30d").strftime("%Y-%m-%d %H:%M-%H:%M")
        }
        response = api.new_lead(data=data)
        assert response == 'Заявка отправлена'
        list_lead = db.get_lead_id(phone=generated_phone, name=generated_name)
        lead_id = list_lead["id"]
        db.delete_lead_id(lead_id)

    def test_lead_negative_regtype(self, api, db):
        #запись на занятие с типом "без записи"
        res = db.get_first_active_id(2)
        active_id = res["id"]
        data = {
            "active_id": active_id,
            "name": "Иван",
            "phone": "79000000000",
            "date": "2025-02-27 11:00-11:30"
        }
        response = api.new_lead(data=data, status=500)
        assert response["message"] == 'У этой актиновности тип без записи'
