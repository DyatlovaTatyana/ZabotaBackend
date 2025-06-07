import pytest
import requests

base_url = "https://api.zabotaservice.ru"
active_id = 2888

def test_get_active_id():
    get_active = requests.get(f"{base_url}/active/{active_id}?expand=registration_type")
    assert get_active.status_code == 200
    # print(get_active.headers)
    assert get_active.headers['Content-Type'] == 'application/json; charset=UTF-8'
    active_info = get_active.json()
    active_type = active_info['registration_type']
    print(active_type)

def test_lead():
    #запись на занятие
    data = {
        "active_id": active_id,
        "name": "Иван",
        "phone": "79000000000",
        "date": "2025-02-27 11:00-11:30"
    }
    create_lead = requests.post(f"{base_url}/active/lead", json=data)
    assert create_lead.status_code == 200
    # print(create_lead.headers)
    assert create_lead.headers['Content-Type'] == 'application/json; charset=UTF-8'