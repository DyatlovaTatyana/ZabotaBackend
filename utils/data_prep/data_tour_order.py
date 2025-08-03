

def generate_order_data(api, db,tour_id=None ):
    if not tour_id:
        tour_id = db.get_first_tour_id()["id"]
    tour_info = api.get_tour(tour_id=tour_id)

    return {
        "timetable_id": tour_info["timetable"][0]["id"],
        "payment_type_id": tour_info["paymentType"][0]["id"],
        "place_start_id": tour_info["placeStart"][0]["id"],
        "tickets": [{
            "type_id": tour_info["ticketType"][0]["id"],
            "count": 2
        }],
        "client_email": "test@mail.ru",
        "client_fio": "Иван Иванов",
        "client_telephone": "+79991234567",
        "url_success": "https://example.com/success",
        "url_fail": "https://example.com/fail"
    }